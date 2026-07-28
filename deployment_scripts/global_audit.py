import os
import json
import sqlite3
from datetime import datetime


ROOT=r"E:\football_v"


result={}

result["version"]="FOOTBALL_AI_OS_V4.0_GLOBAL_AUDIT"

result["time"]=str(datetime.now())


# --------------------
# 核心路径检查
# --------------------

paths={

"checkpoint":
r"E:\football_v\checkpoint",

"production_orchestrator":
r"E:\football_v\32_PRODUCTION_ORCHESTRATOR",

"production_runtime":
r"E:\football_v\44_PRODUCTION_PREDICTION_RUNTIME",

"prediction_output":
r"E:\football_v\14_OPERATION_LAYER\output\prediction_result.json",

"learning_database":
r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db",

"decision_layer":
r"E:\football_v\08_DECISION_INTELLIGENCE_LAYER",

"feedback_connector":
r"E:\football_v\08_DECISION_INTELLIGENCE_LAYER\feedback_interface\feedback_connector.py",

"feedback_receiver":
r"E:\football_v\07_AI_ORCHESTRATION_LAYER\learning_hook\feedback_receiver.py",

"feedback_engine":
r"E:\football_v\31_SELF_LEARNING_ENGINE\feedback_engine.py",

"model_update":
r"E:\football_v\31_SELF_LEARNING_ENGINE\model_update_engine.py",

"calibration_engine":
r"E:\football_v\28_PROBABILITY_CALIBRATION_ENGINE\calibration_engine.py"

}


result["paths"]={}

for k,v in paths.items():

    result["paths"][k]={
        "exists":os.path.exists(v),
        "path":v
    }



# --------------------
# Prediction检查
# --------------------

prediction=paths["prediction_output"]

if os.path.exists(prediction):

    with open(prediction,"r",encoding="utf-8") as f:
        data=json.load(f)

    result["prediction"]={

        "exists":True,

        "keys":list(data.keys()),

        "decision":data.get("decision"),

        "status":data.get("status"),

        "model_version":data.get("version")

    }

else:

    result["prediction"]={"exists":False}



# --------------------
# 数据库检查
# --------------------

db=paths["learning_database"]

if os.path.exists(db):

    conn=sqlite3.connect(db)

    cursor=conn.cursor()

    cursor.execute(
        "select name from sqlite_master where type='table'"
    )

    tables=[
        x[0] for x in cursor.fetchall()
    ]


    dbinfo={
        "tables":tables
    }


    if "prediction_feedback" in tables:

        cursor.execute(
        "select count(*) from prediction_feedback"
        )

        dbinfo["prediction_feedback_count"]=cursor.fetchone()[0]


    conn.close()

    result["database"]=dbinfo

else:

    result["database"]={"exists":False}




# --------------------
# Registry扫描
# --------------------

registry=[]

for root,dirs,files in os.walk(ROOT):

    for f in files:

        if "registry" in f.lower():

            registry.append(
                os.path.join(root,f)
            )


result["registry_files"]=registry[:50]



# --------------------
# Checkpoint
# --------------------

checkpoint=[]

for root,dirs,files in os.walk(
r"E:\football_v\checkpoint"
):

    for f in files:

        checkpoint.append(f)


result["checkpoint_files"]=checkpoint



# --------------------
# 学习相关模块
# --------------------

learning=[]

keywords=[
"feedback",
"learning",
"calibration",
"self_learning",
"roi"
]


for root,dirs,files in os.walk(ROOT):

    for f in files:

        low=f.lower()

        if any(x in low for x in keywords):

            learning.append(
                os.path.join(root,f)
            )


result["learning_related_files"]=learning[:100]



result["status"]="AUDIT_COMPLETE"


with open(
r"E:\football_v\reports\FOOTBALL_AI_OS_V4_GLOBAL_AUDIT.json",
"w",
encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        indent=4,
        ensure_ascii=False
    )


print(
json.dumps(
result,
indent=4,
ensure_ascii=False
)
)

