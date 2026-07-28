import sqlite3
import os
import json
import shutil
from datetime import datetime


SOURCE_DB = r"E:\football_v\01_DATA_LAYER\database\match_data.db"

TARGET_DB = r"E:\football_v\00_SYSTEM_OS\01_DATA_LAYER\database\match_data.db"

BACKUP_DIR = r"E:\football_v\99_Documentation\checkpoints"

REPORT_DIR = r"E:\football_v\99_Documentation\reports"


BACKUP_DB = os.path.join(
    BACKUP_DIR,
    "archive_match_data_before_v22.db"
)

REPORT_FILE = os.path.join(
    REPORT_DIR,
    "DATABASE_UNIFIED_MIGRATION_V2.2_REPORT.json"
)


def ensure_dirs():

    os.makedirs(BACKUP_DIR, exist_ok=True)

    os.makedirs(REPORT_DIR, exist_ok=True)


def backup_target():

    if os.path.exists(TARGET_DB):

        shutil.copy2(
            TARGET_DB,
            BACKUP_DB
        )

        print(
            "Backup created:",
            BACKUP_DB
        )


def get_tables(conn):

    cur = conn.cursor()

    rows = cur.execute(
        """
        SELECT name 
        FROM sqlite_master
        WHERE type='table'
        """
    ).fetchall()

    return [
        r[0]
        for r in rows
    ]


def get_counts(conn,tables):

    result={}

    cur=conn.cursor()

    for t in tables:

        try:

            result[t]=cur.execute(
                f"SELECT COUNT(*) FROM '{t}'"
            ).fetchone()[0]

        except:

            result[t]="ERROR"

    return result



def migrate():

    print("="*60)

    print(
        "Football AI OS Database Unified Migration V2.2"
    )

    print("="*60)



    ensure_dirs()


    backup_target()



    if not os.path.exists(SOURCE_DB):

        raise Exception(
            "Source database missing"
        )


    if os.path.exists(TARGET_DB):

        os.remove(TARGET_DB)



    src=sqlite3.connect(
        SOURCE_DB
    )

    dst=sqlite3.connect(
        TARGET_DB
    )


    tables=[t for t in get_tables(src) if t != "sqlite_sequence"]


    print(
        "Tables:",
        len(tables)
    )


    for table in tables:


        print(
            "Migrating:",
            table
        )


        schema=src.execute(
            f"""
            SELECT sql 
            FROM sqlite_master
            WHERE type='table'
            AND name='{table}'
            """
        ).fetchone()[0]


        dst.execute(schema)


        rows=src.execute(
            f"SELECT * FROM '{table}'"
        ).fetchall()


        if rows:


            placeholders=",".join(
                ["?"]*len(rows[0])
            )


            dst.executemany(
                f"""
                INSERT INTO '{table}'
                VALUES ({placeholders})
                """,
                rows
            )



    dst.commit()


    source_counts=get_counts(
        src,
        tables
    )


    target_tables=get_tables(dst)

    target_counts=get_counts(
        dst,
        target_tables
    )


    status=True


    for t in tables:

        if source_counts.get(t)!=target_counts.get(t):

            status=False



    report={

        "time":
        str(datetime.now()),


        "source":
        SOURCE_DB,


        "target":
        TARGET_DB,


        "tables":
        tables,


        "source_counts":
        source_counts,


        "target_counts":
        target_counts,


        "status":
        "PASS" if status else "FAIL"

    }


    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )


    print()

    print(
        "Migration Status:",
        report["status"]
    )


    print(
        "Report:",
        REPORT_FILE
    )



    src.close()

    dst.close()



if __name__=="__main__":

    migrate()

