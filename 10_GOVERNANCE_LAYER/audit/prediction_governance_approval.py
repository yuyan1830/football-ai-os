import csv
import json
from datetime import datetime
from pathlib import Path


BASE=Path(r"E:\football_v")

audit=BASE/"10_GOVERNANCE_LAYER/audit"
registry=BASE/"10_GOVERNANCE_LAYER/registry"
checkpoint=BASE/"10_GOVERNANCE_LAYER/checkpoint"


now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")


assets=[

["prediction_service.db",
"04_PREDICTION_LAYER",
"SERVICE_DATABASE",
"KEEP_CURRENT",
"LOW",
"APPROVED"],

["prediction_runtime.db",
"04_PREDICTION_LAYER",
"RUNTIME_DATABASE",
"KEEP_CURRENT",
"LOW",
"APPROVED"],

["api_runtime.db",
"04_PREDICTION_LAYER",
"API_DATABASE",
"KEEP_CURRENT",
"LOW",
"APPROVED"]

]


with open(
audit/"Prediction_Layer_Governance_Approval_V1.0.csv",
"w",
newline="",
encoding="utf-8"
) as f:

    writer=csv.writer(f)

    writer.writerow(
    [
    "Asset",
    "Layer",
    "Asset_Type",
    "Decision",
    "Risk",
    "Status",
    "Validation_Time"
    ])

    for a in assets:
        writer.writerow(a+[now])



with open(
registry/"Prediction_Layer_Final_Asset_Register_V1.0.csv",
"w",
newline="",
encoding="utf-8"
) as f:

    writer=csv.writer(f)

    writer.writerow(
    [
    "Asset",
    "Ownership",
    "Lifecycle",
    "Runtime_Status"
    ])

    for a in assets:
        writer.writerow(
        [
        a[0],
        "CURRENT",
        "ACTIVE",
        "ACTIVE"
        ])



data={

"Checkpoint":
"PREDICTION_LAYER_V1.2",

"Architecture":
"Football_AI_OS_Betting_Intelligence_System_Omega_V3.2",

"Rule_Source":
"CLAUDE.md",

"Status":
"PREDICTION_GOVERNANCE_APPROVED",

"Completed":[

"Prediction Asset Discovery",

"Database Inventory",

"Schema Validation",

"Governance Approval"

],

"Pending":[

"Market Layer Integration"

],

"Modification":{

"Database_Content":False,

"Business_Logic":False,

"Model_Code":False

}

}


with open(
checkpoint/"Checkpoint_PREDICTION_LAYER_V1.2.json",
"w",
encoding="utf-8"
) as f:

    json.dump(
    data,
    f,
    indent=4,
    ensure_ascii=False
    )


print("PREDICTION GOVERNANCE APPROVED")

