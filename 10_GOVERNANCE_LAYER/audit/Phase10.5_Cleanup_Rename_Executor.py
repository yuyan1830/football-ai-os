import os
import csv
from datetime import datetime


ROOT = r"E:\football_v"

AUDIT_PATH = os.path.join(
    ROOT,
    "10_GOVERNANCE_LAYER",
    "audit"
)

REGISTRY_PATH = os.path.join(
    ROOT,
    "10_GOVERNANCE_LAYER",
    "registry"
)


PLAN = os.path.join(
    AUDIT_PATH,
    "Asset_Cleanup_Action_Plan_V1.0.csv"
)


REGISTER = os.path.join(
    REGISTRY_PATH,
    "Unused_Asset_Register_V1.0.csv"
)


LOCKED = {

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
"99_DOCUMENTATION",

"CLAUDE.md",

"Football_AI_OS_Legacy_Asset_Index_V1.0",

"Football_AI_OS_Betting_Intelligence_System_Omega_V3.2_Baseline.md"

}


os.makedirs(
    REGISTRY_PATH,
    exist_ok=True
)


records = []


with open(
    PLAN,
    "r",
    encoding="utf-8-sig"
) as f:


    reader = csv.DictReader(f)


    for row in reader:


        if row["Action"] != "RENAME":
            continue


        old_path = row["Original_Path"]


        if not os.path.exists(old_path):
            continue


        parts = old_path.split(os.sep)


        if any(
            x in LOCKED
            for x in parts
        ):
            continue



        new_path = os.path.join(

            os.path.dirname(old_path),

            row["New_Name"]

        )


        if os.path.exists(new_path):

            print(
                "SKIP EXISTS:",
                new_path
            )

            continue



        os.rename(
            old_path,
            new_path
        )


        records.append({

            "Old_Path":
                old_path,

            "New_Path":
                new_path,

            "Status":
                "RENAMED",

            "Reason":
                row["Reason"],

            "Time":
                str(datetime.now())

        })



with open(

    REGISTER,

    "w",

    newline="",

    encoding="utf-8"

) as f:


    writer = csv.DictWriter(

        f,

        fieldnames=[
            "Old_Path",
            "New_Path",
            "Status",
            "Reason",
            "Time"
        ]

    )


    writer.writeheader()

    writer.writerows(records)



print(
    "PHASE10.5 PART3 CLEANUP RENAME COMPLETED"
)

print(
    "Renamed:",
    len(records)
)

print(
    "Register:",
    REGISTER
)

