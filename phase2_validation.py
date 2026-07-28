import os
import json
from datetime import datetime


root=r"E:\football_v"


result={
    "project":"Football AI OS",
    "phase":"Phase 2 Feature Store Integration Final Validation",
    "time":str(datetime.now()),

    "checks":{

        "feature_store":
        os.path.exists(
            root+r"\04_Data_Processing_AI\feature_store"
        ),

        "model_layer":
        os.path.exists(
            root+r"\05_MODEL_AI\MODEL_LAYER"
        ),

        "feature_count":
        len(
            [
            f for f in os.listdir(
            root+r"\04_Data_Processing_AI\feature_store"
            )
            if f.endswith(".py")
            ]
        ),

        "connector":
        os.path.exists(
        root+r"\05_MODEL_AI\MODEL_LAYER\feature_store_connector.py"
        )
    }
}


report=root+r"\99_DOCUMENTATION\reports\PHASE2_FEATURE_STORE_VALIDATION_V1.0.json"


with open(report,"w",encoding="utf-8") as f:
    json.dump(
        result,
        f,
        indent=2,
        ensure_ascii=False
    )


print(json.dumps(result,indent=2,ensure_ascii=False))

print("")
print("REPORT:")
print(report)