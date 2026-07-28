import sqlite3
import json
import os
from datetime import datetime


db=r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db"


result={
    "version":"FOOTBALL_AI_OS_V4.0_LEARNING_PIPELINE_FINAL_AUDIT",
    "time":str(datetime.now()),
    "database":db
}


# database

if os.path.exists(db):

    conn=sqlite3.connect(db)

    cursor=conn.cursor()


    tables=cursor.execute(
        "select name from sqlite_master where type='table'"
    ).fetchall()


    result["tables"]=[
        x[0] for x in tables
    ]


    schema={}


    for t in result["tables"]:

        cols=cursor.execute(
            f"pragma table_info({t})"
        ).fetchall()


        schema[t]=[
            {
                "name":c[1],
                "type":c[2]
            }
            for c in cols
        ]


    result["schema"]=schema



    if "prediction_feedback" in result["tables"]:

        result["prediction_feedback_count"]=cursor.execute(
            "select count(*) from prediction_feedback"
        ).fetchone()[0]


    conn.close()


else:

    result["database_status"]="MISSING"



print(
    json.dumps(
        result,
        indent=4,
        ensure_ascii=False
    )
)
