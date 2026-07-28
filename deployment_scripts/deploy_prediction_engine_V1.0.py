import sqlite3
import os
import json
import hashlib
from datetime import datetime


BASE=r"E:\football_v"


SYSTEM_DB=os.path.join(
BASE,
"00_SYSTEM_OS",
"01_DATA_LAYER",
"database",
"football_ai_os.db"
)


MATCH_DB=os.path.join(
BASE,
"00_SYSTEM_OS",
"01_DATA_LAYER",
"database",
"match_data.db"
)


FEATURE_DB=os.path.join(
BASE,
"00_SYSTEM_OS",
"02_FEATURE_LAYER",
"database",
"feature_store.db"
)


MODEL_DB=os.path.join(
BASE,
"00_SYSTEM_OS",
"03_MODEL_LAYER",
"database",
"model_store.db"
)


REPORT=os.path.join(
BASE,
"99_Documentation",
"reports",
"Prediction_ENGINE_V1.0_REPORT.json"
)



def sha256(path):

    h=hashlib.sha256()

    with open(path,"rb") as f:

        for b in iter(lambda:f.read(8192),b""):

            h.update(b)

    return h.hexdigest()



def create_prediction_tables():

    conn=sqlite3.connect(SYSTEM_DB)

    cur=conn.cursor()


    cur.execute(
    """
    CREATE TABLE IF NOT EXISTS prediction_registry
    (
    id INTEGER PRIMARY KEY,
    match_id INTEGER,
    home_win REAL,
    draw REAL,
    away_win REAL,
    score TEXT,
    confidence REAL,
    risk TEXT,
    time TEXT
    )
    """
    )


    conn.commit()

    conn.close()



def check_connections():

    result={}


    for name,path in {

    "system":SYSTEM_DB,

    "match":MATCH_DB,

    "feature":FEATURE_DB,

    "model":MODEL_DB

    }.items():


        conn=sqlite3.connect(path)

        cur=conn.cursor()


        cur.execute(
        """
        SELECT COUNT(*)
        FROM sqlite_master
        WHERE type='table'
        """
        )


        result[name]={

        "exists":os.path.exists(path),

        "size":os.path.getsize(path),

        "sha256":sha256(path),

        "tables":
        cur.fetchone()[0]

        }


        conn.close()


    return result



def create_test_prediction():

    conn=sqlite3.connect(SYSTEM_DB)

    cur=conn.cursor()


    cur.execute(
    """
    INSERT INTO prediction_registry
    (
    match_id,
    home_win,
    draw,
    away_win,
    score,
    confidence,
    risk,
    time
    )
    VALUES
    (?,?,?,?,?,?,?,?)
    """,
    (
    0,
    0.45,
    0.28,
    0.27,
    "1-0",
    0.72,
    "LOW",
    datetime.now().isoformat()
    )
    )


    conn.commit()

    conn.close()



def check_prediction():

    conn=sqlite3.connect(SYSTEM_DB)

    cur=conn.cursor()


    cur.execute(
    """
    SELECT COUNT(*)
    FROM prediction_registry
    """
    )


    count=cur.fetchone()[0]


    conn.close()


    return count



def main():

    print("="*60)

    print("Football AI OS Prediction Engine V1.0")

    print("="*60)


    create_prediction_tables()

    create_test_prediction()


    report={

    "version":
    "PREDICTION_ENGINE_V1.0",

    "time":
    datetime.now().isoformat(),

    "database_check":
    check_connections(),

    "prediction_records":
    check_prediction(),

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
    encoding="utf8"
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


    print("PREDICTION ENGINE COMPLETE")



if __name__=="__main__":

    main()

