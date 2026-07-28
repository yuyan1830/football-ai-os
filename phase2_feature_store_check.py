import os
import json
from datetime import datetime


BASE = r"E:\football_v"

FEATURE_STORE = os.path.join(
    BASE,
    "04_Data_Processing_AI",
    "feature_store"
)

MODEL_LAYER = os.path.join(
    BASE,
    "05_MODEL_AI",
    "MODEL_LAYER"
)


result = {
    "project": "Football AI OS",
    "phase": "Phase 2 Feature Store Integration Validation",
    "time": str(datetime.now()),
    "checks": {}
}


# Feature Store
result["checks"]["feature_store_exists"] = os.path.exists(
    FEATURE_STORE
)

# Model Layer
result["checks"]["model_layer_exists"] = os.path.exists(
    MODEL_LAYER
)


# Feature Store files
if os.path.exists(FEATURE_STORE):
    files = []
    for root, dirs, fs in os.walk(FEATURE_STORE):
        for f in fs:
            if f.endswith(".py"):
                files.append(
                    os.path.join(root,f)
                )

    result["checks"]["feature_store_python_files"] = len(files)


# Model connection
connector = os.path.join(
    MODEL_LAYER,
    "feature_store_connector.py"
)

result["checks"]["model_feature_connector"] = os.path.exists(
    connector
)


report = os.path.join(
    BASE,
    "99_DOCUMENTATION",
    "reports",
    "PHASE2_FEATURE_STORE_VALIDATION_V1.0.json"
)


with open(
    report,
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        result,
        f,
        indent=2,
        ensure_ascii=False
    )


print(json.dumps(
    result,
    indent=2,
    ensure_ascii=False
))