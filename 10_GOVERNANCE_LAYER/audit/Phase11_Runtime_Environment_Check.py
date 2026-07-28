import os
import sys
import json
from datetime import datetime


ROOT = r"E:\football_v"


LAYERS = [

    "01_DATA_LAYER",
    "02_FEATURE_LAYER",
    "03_MODEL_LAYER",
    "04_PREDICTION_LAYER",
    "05_MARKET_LAYER",
    "06_RISK_LAYER",
    "07_LEARNING_LAYER",
    "08_DECISION_LAYER",
    "09_APPLICATION_LAYER",
    "10_GOVERNANCE_LAYER",
    "11_SIMULATION_LAYER",
    "12_API_LAYER",
    "13_TEST_LAYER",
    "99_DOCUMENTATION"

]


AUDIT_PATH = os.path.join(
    ROOT,
    "10_GOVERNANCE_LAYER",
    "audit"
)


CHECKPOINT_PATH = os.path.join(
    ROOT,
    "10_GOVERNANCE_LAYER",
    "checkpoint"
)


print(
    "PHASE11 PART1 RUNTIME VALIDATION START"
)


result = {

    "Phase":
        "PHASE11_OPERATION_READY_PART1",

    "Architecture":
        "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2",

    "Baseline":
        "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2_Baseline.md",

    "Legacy_Source":
        "Football_AI_OS_Legacy_Asset_Index_V1.0",

    "Rule_Source":
        "CLAUDE.md",

    "Python_Version":
        sys.version,

    "Layers": {},

    "Validation_Time":
        str(datetime.now())

}



for layer in LAYERS:

    path = os.path.join(
        ROOT,
        layer
    )

    result["Layers"][layer] = {

        "Exists":
            os.path.exists(path)

    }


for k,v in result["Layers"].items():

    print(
        k,
        "PASS" if v["Exists"] else "FAIL"
    )


os.makedirs(
    AUDIT_PATH,
    exist_ok=True
)


output = os.path.join(
    AUDIT_PATH,
    "Phase11_Runtime_Environment_Check_V1.0.json"
)


with open(
    output,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        indent=4,
        ensure_ascii=False
    )


print("")
print(
    "PHASE11 PART1 COMPLETED"
)

print(
    output
)

