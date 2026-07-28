import os
import csv
from datetime import datetime


ROOT = r"E:\football_v"


AUDIT_PATH = os.path.join(
    ROOT,
    "10_GOVERNANCE_LAYER",
    "audit"
)


OUTPUT = os.path.join(
    AUDIT_PATH,
    "Asset_Cleanup_Action_Plan_V1.0.csv"
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


ARCHIVE_KEYWORDS = [

"old",
"backup",
"bak",
"legacy",
"copy",
"history"

]


TEMP_KEYWORDS = [

"temp",
"tmp",
"debug",
"cache"

]


results = []


for root, dirs, files in os.walk(ROOT):


    relative_parts = root.split(os.sep)


    if any(
        item in LOCKED
        for item in relative_parts
    ):
        continue


    for name in dirs + files:


        if name in LOCKED:
            continue


        path = os.path.join(
            root,
            name
        )


        lower = name.lower()


        action = None
        new_name = None
        reason = None


        if any(
            k in lower
            for k in TEMP_KEYWORDS
        ):

            action = "RENAME"

            new_name = (
                "TEMP_"
                + name
            )

            reason = (
                "Temporary asset"
            )


        elif any(
            k in lower
            for k in ARCHIVE_KEYWORDS
        ):

            action = "RENAME"

            new_name = (
                "ARCHIVE_"
                + name
            )

            reason = (
                "Historical asset"
            )


        else:

            continue



        results.append({

            "Original_Path":
                path,

            "Original_Name":
                name,

            "New_Name":
                new_name,

            "Action":
                action,

            "Reason":
                reason,

            "Validation_Time":
                str(datetime.now())

        })



with open(

    OUTPUT,

    "w",

    newline="",

    encoding="utf-8"

) as f:


    writer = csv.DictWriter(

        f,

        fieldnames=[
            "Original_Path",
            "Original_Name",
            "New_Name",
            "Action",
            "Reason",
            "Validation_Time"
        ]

    )


    writer.writeheader()

    writer.writerows(results)



print(
    "PHASE10.5 PART2 CLEANUP PLAN GENERATED"
)

print(
    "Candidates:",
    len(results)
)

