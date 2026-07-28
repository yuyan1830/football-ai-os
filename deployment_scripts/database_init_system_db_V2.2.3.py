import sqlite3
import os
import json
import hashlib
from datetime import datetime


BASE = r"E:\football_v"


SYSTEM_DB = os.path.join(
    BASE,
    "00_SYSTEM_OS",
    "01_DATA_LAYER",
    "database",
    "football_ai_os.db"
)


REPORT = os.path.join(
    BASE,
    "99_Documentation",
    "reports",
    "DATABASE_SYSTEM_INITIALIZE_V2.2.3_REPORT.json"
)


DATABASES = {
    "football_ai_os": SYSTEM_DB,

    "match_data":
    os.path.join(
        BASE,
        "00_SYSTEM_OS",
        "01_DATA_LAYER",
        "database",
        "match_data.db"
    ),

    "feature_store":
    os.path.join(
        BASE,
        "00_SYSTEM_OS",
        "02_FEATURE_LAYER",
        "database",
        "feature_store.db"
    ),

    "model_store":
    os.path.join(
        BASE,
        "00_SYSTEM_OS",
        "03_MODEL_LAYER",
        "database",
        "model_store.db"
    )
}


def sha256(path):

    if not os.path.exists(path):
        return None

    h = hashlib.sha256()

    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(8192),b""):
            h.update(chunk)

    return h.hexdigest()


def create_database():

    os.makedirs(
        os.path.dirname(SYSTEM_DB),
        exist_ok=True
    )

    conn = sqlite3.connect(SYSTEM_DB)

    cur = conn.cursor()


    tables = {

    "system_registry":
    """
    CREATE TABLE IF NOT EXISTS system_registry(
        id INTEGER PRIMARY KEY,
        system_name TEXT,
        version TEXT,
        status TEXT,
        created_time TEXT
    )
    """,

    "database_registry":
    """
    CREATE TABLE IF NOT EXISTS database_registry(
        id INTEGER PRIMARY KEY,
        database_name TEXT,
        database_path TEXT,
        database_role TEXT,
        version TEXT,
        status TEXT,
        hash TEXT,
        update_time TEXT
    )
    """,

    "model_registry":
    """
    CREATE TABLE IF NOT EXISTS model_registry(
        id INTEGER PRIMARY KEY,
        model_name TEXT,
        model_version TEXT,
        status TEXT,
        created_time TEXT
    )
    """,

    "runtime_registry":
    """
    CREATE TABLE IF NOT EXISTS runtime_registry(
        id INTEGER PRIMARY KEY,
        service_name TEXT,
        status TEXT,
        heartbeat TEXT
    )
    """,

    "task_registry":
    """
    CREATE TABLE IF NOT EXISTS task_registry(
        id INTEGER PRIMARY KEY,
        task_name TEXT,
        status TEXT,
        last_run TEXT
    )
    """
    }


    for name,sql in tables.items():
        cur.execute(sql)


    cur.execute(
    """
    INSERT INTO system_registry
    (
    system_name,
    version,
    status,
    created_time
    )
    VALUES
    (?,?,?,?)
    """,
    (
    "Football AI OS",
    "DATABASE_V2.2.3",
    "ACTIVE",
    datetime.now().isoformat()
    )
    )


    for name,path in DATABASES.items():

        if name=="football_ai_os":
            role="SYSTEM"

        elif name=="match_data":
            role="DATA"

        elif name=="feature_store":
            role="FEATURE"

        else:
            role="MODEL"


        cur.execute(
        """
        INSERT INTO database_registry
        (
        database_name,
        database_path,
        database_role,
        version,
        status,
        hash,
        update_time
        )
        VALUES
        (?,?,?,?,?,?,?)
        """,
        (
        name,
        path,
        role,
        "V2.2",
        "READY",
        sha256(path),
        datetime.now().isoformat()
        )
        )


    conn.commit()
    conn.close()



def generate_report():

    conn=sqlite3.connect(SYSTEM_DB)

    cur=conn.cursor()

    tables={}

    for row in cur.execute(
        "select name from sqlite_master where type='table'"
    ):

        t=row[0]

        count=cur.execute(
            f"select count(*) from {t}"
        ).fetchone()[0]

        tables[t]=count


    conn.close()


    report={

    "version":
    "DATABASE_SYSTEM_INITIALIZE_V2.2.3",

    "time":
    datetime.now().isoformat(),

    "database":
    SYSTEM_DB,

    "tables":
    tables,

    "status":
    "PASS"

    }


    os.makedirs(
        os.path.dirname(REPORT),
        exist_ok=True
    )


    with open(
        REPORT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )


    print(json.dumps(
        report,
        indent=4,
        ensure_ascii=False
    ))



if __name__=="__main__":

    print("="*60)
    print("Football AI OS System Database Initialize V2.2.3")
    print("="*60)

    create_database()

    generate_report()

    print("DATABASE SYSTEM INITIALIZE COMPLETE")
