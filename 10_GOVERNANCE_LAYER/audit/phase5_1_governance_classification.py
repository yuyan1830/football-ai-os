import os
import csv
import json
from datetime import datetime


BASE = r"E:\football_v"

REGISTRY = r"E:\football_v\10_GOVERNANCE_LAYER\registry"
AUDIT = r"E:\football_v\10_GOVERNANCE_LAYER\audit"
CHECKPOINT = r"E:\football_v\10_GOVERNANCE_LAYER\checkpoint"


SOURCE_FILES = [

(
"market_value.db",
r"E:\football_v\05_MARKET_LAYER\database\market_value.db",
"05_MARKET_LAYER"
),

(
"risk_manager.db",
r"E:\football_v\06_RISK_LAYER\database\risk_manager.db",
"06_RISK_LAYER"
),

(
"learning_feedback.db",
r"E:\football_v\07_LEARNING_LAYER\database\learning_feedback.db",
"07_LEARNING_LAYER"
),

(
"decision_history.db",
r"E:\football_v\08_DECISION_LAYER\database\decision_history.db",
"08_DECISION_LAYER"
),

(
"application_runtime.db",
r"E:\football_v\09_APPLICATION_LAYER\runtime\application_runtime.db",
"09_APPLICATION_LAYER"
)

]


def classify(layer,name):

    if "runtime" in name:
        return (
            "RUNTIME_ASSET",
            "CURRENT",
            "ACTIVE",
            "LOW"
        )

    if "history" in name:
        return (
            "HISTORY_ASSET",
            "CURRENT",
            "ACTIVE",
            "LOW"
        )


    if layer=="06_RISK_LAYER":

        return (
            "RISK_GOVERNANCE_ASSET",
            "CURRENT",
            "ACTIVE",
            "MEDIUM"
        )


    if layer=="07_LEARNING_LAYER":

        return (
            "LEARNING_ASSET",
            "CURRENT",
            "ACTIVE",
            "MEDIUM"
        )


    if layer=="05_MARKET_LAYER":

        return (
            "MARKET_ASSET",
            "CURRENT",
            "ACTIVE",
            "MEDIUM"
        )


    if layer=="08_DECISION_LAYER":

        return (
            "DECISION_ASSET",
            "CURRENT",
            "ACTIVE",
            "MEDIUM"
        )


    return (
        "CURRENT_ASSET",
        "CURRENT",
        "ACTIVE",
        "LOW"
    )



records=[]


for name,path,layer in SOURCE_FILES:

    exists=os.path.exists(path)

    asset_type,ownership,status,risk=classify(
        layer,
        name
    )


    records.append([

        name,

        path,

        layer,

        asset_type,

        ownership,

        status,

        risk,

        "OMEGA_V3.2_CURRENT",

        exists,

        datetime.now()

    ])





with open(
os.path.join(
REGISTRY,
"Phase5_Governance_Register_V1.0.csv"),
"w",
newline="",
encoding="utf-8") as f:


    w=csv.writer(f)

    w.writerow([

        "Asset",
        "Path",
        "Layer",
        "Asset_Type",
        "Ownership",
        "Lifecycle_Status",
        "Risk",
        "Architecture_Source",
        "Exists",
        "Validation_Time"

    ])

    w.writerows(records)





with open(
os.path.join(
AUDIT,
"Phase5_Governance_Report_V1.0.md"),
"w",
encoding="utf-8") as f:


    f.write(
f"""
# Phase5 Governance Report V1.0


Architecture:

Football_AI_OS_Betting_Intelligence_System_Omega_V3.2


Legacy Reference:

Football_AI_OS_Legacy_Asset_Index_V1.0


Rule Source:

CLAUDE.md


## Classification Result


Total Assets:

{len(records)}


Status:

GOVERNANCE_CLASSIFICATION_COMPLETED


Modification:

- Database_Content: false
- Business_Logic: false
- Model_Code: false


Validation Time:

{datetime.now()}

"""
)






checkpoint_data={


"Checkpoint":
"PHASE5_BATCH_V1.1",


"Architecture":
"Football_AI_OS_Betting_Intelligence_System_Omega_V3.2",


"Legacy_Source":
"Football_AI_OS_Legacy_Asset_Index_V1.0",


"Rule_Source":
"CLAUDE.md",


"Status":
"GOVERNANCE_CLASSIFICATION_COMPLETED",


"Completed":[

"Asset Discovery",

"Database Inventory",

"SQLite Validation",

"Hash Validation",

"Governance Classification"

],


"Pending":[

"Layer Approval"

],


"Modification":{

"Database_Content":False,

"Business_Logic":False,

"Model_Code":False

}

}



with open(
os.path.join(
CHECKPOINT,
"Checkpoint_PHASE5_BATCH_V1.1.json"),
"w",
encoding="utf-8") as f:


    json.dump(
        checkpoint_data,
        f,
        indent=4,
        ensure_ascii=False
    )



print("PHASE5.1_GOVERNANCE_CLASSIFICATION_COMPLETED")

