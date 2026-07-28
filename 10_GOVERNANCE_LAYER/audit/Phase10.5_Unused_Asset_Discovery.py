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
    "Unused_Asset_Candidate_List_V1.0.csv"
)


IGNORE = {

    ".git",

    "__pycache__",

    "node_modules"

}


KEYWORDS = [

    "old",

    "backup",

    "bak",

    "temp",

    "tmp",

    "test_old",

    "legacy",

    "copy",

    "debug"

]


results = []


for root, dirs, files in os.walk(ROOT):


    dirs[:] = [
        d for d in dirs
        if d not in IGNORE
    ]


    for name in dirs + files:


        path = os.path.join(
            root,
            name
        )


        lower = name.lower()


        if any(
            k in lower
            for k in KEYWORDS
        ):


            if name.startswith(
                (
                    "01_",
                    "02_",
                    "03_",
                    "04_",
                    "05_",
                    "06_",
                    "07_",
                    "08_",
                    "09_",
                    "10_",
                    "11_",
                    "12_",
                    "13_",
                    "99_"
                )
            ):

                decision = "REVIEW_ONLY"

            else:

                decision = "CANDIDATE"


            results.append({

                "Path": path,

                "Name": name,

                "Type":
                    "DIR"
                    if os.path.isdir(path)
                    else "FILE",

                "Decision":
                    decision,

                "Suggested_Status":
                    "UNUSED_OR_ARCHIVE",

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

        fieldnames=results[0].keys()
        if results
        else [
            "Path",
            "Name",
            "Type",
            "Decision",
            "Suggested_Status",
            "Validation_Time"
        ]

    )


    writer.writeheader()

    writer.writerows(results)



print(
    "PHASE10.5 UNUSED ASSET DISCOVERY COMPLETED"
)

print(
    "Candidates:",
    len(results)
)

