import os
import json
from datetime import datetime

files=[
r"E:\football_v\08_DECISION_INTELLIGENCE_LAYER\feedback_interface\feedback_connector.py",
r"E:\football_v\07_AI_ORCHESTRATION_LAYER\learning_hook\feedback_receiver.py",
r"E:\football_v\31_SELF_LEARNING_ENGINE\feedback_engine.py"
]

result={
    "version":"FOOTBALL_AI_OS_V4.0_FEEDBACK_PIPELINE_COMPONENT_AUDIT",
    "time":str(datetime.now()),
    "files":{}
}

for f in files:
    item={
        "exists":os.path.exists(f),
        "sqlite_reference":False,
        "prediction_feedback_reference":False,
        "insert_reference":False,
        "update_reference":False
    }

    if os.path.exists(f):
        txt=open(f,"r",encoding="utf-8").read()

        item["sqlite_reference"]="sqlite" in txt.lower()
        item["prediction_feedback_reference"]="prediction_feedback" in txt.lower()
        item["insert_reference"]="insert" in txt.lower()
        item["update_reference"]="update" in txt.lower()

    result["files"][f]=item

print(json.dumps(result,indent=4,ensure_ascii=False))
