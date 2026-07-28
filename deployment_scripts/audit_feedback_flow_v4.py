import os
import json
import sqlite3
from datetime import datetime


paths = {
    "prediction_result":
        r"E:\football_v\14_OPERATION_LAYER\output\prediction_result.json",

    "feedback_connector":
        r"E:\football_v\08_DECISION_INTELLIGENCE_LAYER\feedback_interface\feedback_connector.py",

    "feedback_receiver":
        r"E:\football_v\07_AI_ORCHESTRATION_LAYER\learning_hook\feedback_receiver.py",

    "feedback_engine":
        r"E:\football_v\31_SELF_LEARNING_ENGINE\feedback_engine.py",

    "model_update_engine":
        r"E:\football_v\31_SELF_LEARNING_ENGINE\model_update_engine.py",

    "learning_database":
        r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db"
}


report = {
    "version":"FOOTBALL_AI_OS_V4.0_FEEDBACK_FLOW_AUDIT",
    "time":str(datetime.now()),
    "items":{}
}


for name,path in paths.items():

    report["items"][name]={
        "path":path,
        "exists":os.path.exists(path)
    }


# check database
db=paths["learning_database"]

if os.path.exists(db):

    try:
        conn=sqlite3.connect(db)
        cursor=conn.cursor()

        cursor.execute(
            "select name from sqlite_master where type='table'"
        )

        tables=[x[0] for x in cursor.fetchall()]

        report["items"]["learning_database"]["tables"]=tables

        conn.close()

    except Exception as e:

        report["items"]["learning_database"]["error"]=str(e)


# check prediction json

p=paths["prediction_result"]

if os.path.exists(p):

    try:

        with open(p,"r",encoding="utf-8") as f:
            data=json.load(f)

        report["items"]["prediction_result"]["keys"]=list(data.keys())

    except Exception as e:

        report["items"]["prediction_result"]["error"]=str(e)



report["status"]="AUDIT_COMPLETE"


out=r"E:\football_v\reports\V4_FEEDBACK_FLOW_AUDIT_REPORT.json"

with open(out,"w",encoding="utf-8") as f:

    json.dump(
        report,
        f,
        ensure_ascii=False,
        indent=4
    )


print(json.dumps(report,ensure_ascii=False,indent=4))

