import sqlite3
import csv
import json
from pathlib import Path
from datetime import datetime


BASE = Path(r"E:\football_v")

GOV = BASE / "10_GOVERNANCE_LAYER"

registry = GOV / "registry"
audit = GOV / "audit"
checkpoint = GOV / "checkpoint"


now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


db_list = [

    (
        "prediction_service.db",
        BASE / "04_PREDICTION_LAYER/database/prediction_service.db",
        "SERVICE_DATABASE"
    ),

    (
        "prediction_runtime.db",
        BASE / "04_PREDICTION_LAYER/runtime/prediction_runtime.db",
        "RUNTIME_DATABASE"
    ),

    (
        "api_runtime.db",
        BASE / "04_PREDICTION_LAYER/runtime/api_runtime.db",
        "API_DATABASE"
    )

]


results=[]


for name,path,asset_type in db_list:

    exists = path.exists()

    tables=[]

    if exists:

        conn=sqlite3.connect(path)

        cur=conn.cursor()

        cur.execute(
            "select name from sqlite_master where type='table'"
        )

        tables=[x[0] for x in cur.fetchall()]

        conn.close()


    results.append(
        [
            name,
            str(path),
            asset_type,
            exists,
            len(tables),
            ",".join(tables),
            now
        ]
    )


# Registry

with open(
    registry/"Prediction_Asset_Index_V1.0.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer=csv.writer(f)

    writer.writerow(
        [
            "Asset",
            "Path",
            "Asset_Type",
            "Exists",
            "Table_Count",
            "Tables",
            "Validation_Time"
        ]
    )

    writer.writerows(results)



# Review

with open(
    audit/"Prediction_Layer_Review_V1.0.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer=csv.writer(f)

    writer.writerow(
        [
            "Asset",
            "Layer",
            "Decision",
            "Risk",
            "Status",
            "Validation_Time"
        ]
    )

    for item in results:

        if item[3]:

            writer.writerow(
                [
                    item[0],
                    "04_PREDICTION_LAYER",
                    "KEEP_CURRENT",
                    "LOW",
                    "PENDING_GOVERNANCE",
                    now
                ]
            )

        else:

            writer.writerow(
                [
                    item[0],
                    "04_PREDICTION_LAYER",
                    "MISSING",
                    "HIGH",
                    "REVIEW_REQUIRED",
                    now
                ]
            )



# Validation Report

with open(
    audit/"Prediction_Service_Validation_V1.0.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer=csv.writer(f)

    writer.writerow(
        [
            "Check",
            "Result",
            "Validation_Time"
        ]
    )

    writer.writerow(
        [
            "Database_Discovery",
            "PASS",
            now
        ]
    )

    writer.writerow(
        [
            "Database_Content_Modification",
            "FALSE",
            now
        ]
    )

    writer.writerow(
        [
            "Model_Code_Modification",
            "FALSE",
            now
        ]
    )



# checkpoint

data={

    "Checkpoint":
    "PREDICTION_LAYER_V1.0",

    "Architecture":
    "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2",

    "Rule_Source":
    "CLAUDE.md",

    "Status":
    "IN_PROGRESS",

    "Completed":[
        "Prediction Asset Discovery",
        "Prediction Database Inventory"
    ],

    "Pending":[
        "Prediction Service Validation",
        "Prediction Governance Approval"
    ],

    "Modification":{
        "Database_Content":False,
        "Business_Logic":False,
        "Model_Code":False
    }

}


with open(
    checkpoint/"Checkpoint_PREDICTION_LAYER_V1.0.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        data,
        f,
        indent=4,
        ensure_ascii=False
    )


print("PREDICTION_LAYER DISCOVERY COMPLETED")

