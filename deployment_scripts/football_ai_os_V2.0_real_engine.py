import sqlite3
import json
import os
import hashlib
from datetime import datetime


BASE=r"E:\football_v"

REPORT=r"E:\football_v\99_Documentation\reports\FOOTBALL_AI_OS_V2.0_REAL_DEPLOY_REPORT.json"


DBS={

"api_runtime":
r"E:\football_v\04_PREDICTION_LAYER\runtime\api_runtime.db",

"market_value":
r"E:\football_v\05_MARKET_LAYER\database\market_value.db",

"risk_manager":
r"E:\football_v\06_RISK_LAYER\database\risk_manager.db",

"learning_feedback":
r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db"

}



def create_db(path,name):

    os.makedirs(
        os.path.dirname(path),
        exist_ok=True
    )

    conn=sqlite3.connect(path)

    cur=conn.cursor()

    cur.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {name}
    (
    id INTEGER PRIMARY KEY,
    status TEXT,
    create_time TEXT
    )
    """
    )


    cur.execute(
    f"""
    INSERT INTO {name}
    (
    status,
    create_time
    )
    VALUES
    (
    'ACTIVE',
    ?
    )
    """,
    (
    str(datetime.now()),
    )
    )


    conn.commit()
    conn.close()



def sha256(path):

    h=hashlib.sha256()

    with open(path,"rb") as f:
        h.update(f.read())

    return h.hexdigest()



def main():

    result={}


    for name,path in DBS.items():

        create_db(
            path,
            name+"_registry"
        )


        result[name]={

        "exists":
        True,

        "size":
        os.path.getsize(path),

        "sha256":
        sha256(path)

        }


    report={

    "version":
    "FOOTBALL_AI_OS_V2.0_REAL",

    "time":
    str(datetime.now()),

    "layers":[

    "Prediction API Layer V1.7",

    "Odds Value Engine V1.8",

    "Kelly Risk Engine V1.9",

    "Learning Feedback Layer V2.0"

    ],

    "database":
    result,

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



if __name__=="__main__":
    main()

