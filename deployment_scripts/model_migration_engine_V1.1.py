import sqlite3
import os
import json
from datetime import datetime


MODEL_DB=r"E:\football_v\00_SYSTEM_OS\03_MODEL_LAYER\database\model_store.db"

REPORT=r"E:\football_v\99_Documentation\reports\MODEL_MIGRATION_V1.1_REPORT.json"



def insert_safe(conn,table,data):

    cur=conn.cursor()

    cur.execute(
    f"PRAGMA table_info({table})"
    )

    cols=[
    x[1]
    for x in cur.fetchall()
    ]


    if not cols:
        return "TABLE_MISSING"


    insert={}


    for k,v in data.items():

        if k in cols:
            insert[k]=v


    if not insert:
        return "NO_MATCH_FIELD"


    cur.execute(
    f"""
    INSERT INTO {table}
    ({','.join(insert.keys())})
    VALUES
    ({','.join(['?']*len(insert))})
    """,
    list(insert.values())
    )


    return "INSERT"



def main():

    print("="*60)

    print("Football AI OS Model Migration V1.1")

    print("="*60)


    conn=sqlite3.connect(MODEL_DB)


    result={}


    models={

    "elo_model":
    "ELO",

    "dixon_coles_model":
    "DIXON_COLES",

    "poisson_model":
    "POISSON",

    "xgboost_model":
    "XGBOOST",

    "fusion_model":
    "FUSION"

    }


    for table,name in models.items():


        status=insert_safe(
        conn,
        table,
        {
        "model_name":name,
        "name":name,
        "version":"V2.2",
        "model_version":"V2.2",
        "status":"ACTIVE",
        "state":"ACTIVE"
        }
        )


        result[table]=status



    insert_safe(
    conn,
    "model_weight",
    {
    "model_name":"FUSION",
    "name":"FUSION",
    "weight":1.0
    }
    )


    insert_safe(
    conn,
    "model_version",
    {
    "version":"V2.2",
    "release":"MODEL_RELEASE"
    }
    )


    conn.commit()


    cur=conn.cursor()


    cur.execute(
    """
    SELECT name FROM sqlite_master
    WHERE type='table'
    """
    )


    tables=[
    x[0]
    for x in cur.fetchall()
    ]


    conn.close()



    report={

    "version":
    "MODEL_MIGRATION_V1.1",

    "time":
    datetime.now().isoformat(),

    "result":
    result,

    "tables":
    tables

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


    print("MODEL MIGRATION V1.1 COMPLETE")


if __name__=="__main__":
    main()

