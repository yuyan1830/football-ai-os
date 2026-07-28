import os
import json
import sqlite3
import hashlib
from datetime import datetime


BASE = r"E:\football_v"

DATABASES = {
    "system_database":
        os.path.join(
            BASE,
            "00_SYSTEM_OS",
            "01_DATA_LAYER",
            "database",
            "football_ai_os.db"
        ),

    "match_database":
        os.path.join(
            BASE,
            "00_SYSTEM_OS",
            "01_DATA_LAYER",
            "database",
            "match_data.db"
        ),

    "feature_database":
        os.path.join(
            BASE,
            "00_SYSTEM_OS",
            "02_FEATURE_LAYER",
            "database",
            "feature_store.db"
        ),

    "model_database":
        os.path.join(
            BASE,
            "00_SYSTEM_OS",
            "03_MODEL_LAYER",
            "database",
            "model_store.db"
        )
}


REPORT_DIR = os.path.join(
    BASE,
    "99_Documentation",
    "reports"
)


REPORT_FILE = os.path.join(
    REPORT_DIR,
    "DATABASE_UNIFIED_VALIDATION_V2.2.1_REPORT.json"
)


def sha256_file(path):

    h = hashlib.sha256()

    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)

    return h.hexdigest()


def inspect_database(path):

    result = {
        "path": path,
        "exists": False,
        "size": 0,
        "tables": [],
        "counts": {},
        "sha256": None
    }

    if not os.path.exists(path):
        return result


    result["exists"] = True
    result["size"] = os.path.getsize(path)
    result["sha256"] = sha256_file(path)


    conn = sqlite3.connect(path)

    cur = conn.cursor()


    cur.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name
        """
    )


    tables = [
        x[0]
        for x in cur.fetchall()
    ]


    result["tables"] = tables


    for table in tables:

        if table == "sqlite_sequence":
            continue

        try:

            cur.execute(
                f"SELECT COUNT(*) FROM [{table}]"
            )

            result["counts"][table] = cur.fetchone()[0]

        except Exception as e:

            result["counts"][table] = str(e)


    conn.close()

    return result



def validate():

    print("=" * 60)
    print("Football AI OS Database Unified Validation V2.2.1")
    print("=" * 60)


    report = {

        "version":
            "DATABASE_UNIFIED_VALIDATION_V2.2.1",

        "time":
            datetime.now().isoformat(),

        "databases": {}
    }


    for name,path in DATABASES.items():

        print("")
        print("Checking:", name)

        info = inspect_database(path)

        report["databases"][name] = info


        if info["exists"]:

            print(
                "PASS:",
                path
            )

            print(
                "Tables:",
                len(info["tables"])
            )

        else:

            print(
                "FAIL:",
                path
            )


    os.makedirs(
        REPORT_DIR,
        exist_ok=True
    )


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


    print("")
    print("=" * 60)
    print("VALIDATION COMPLETE")
    print("REPORT:")
    print(REPORT_FILE)
    print("=" * 60)



if __name__ == "__main__":

    validate()

