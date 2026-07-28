import csv
from datetime import datetime


src=r"E:\football_v\10_GOVERNANCE_LAYER\audit\Database_Asset_Classification_V1.0.csv"

out=r"E:\football_v\10_GOVERNANCE_LAYER\migration\Database_Migration_Decision_V1.0.csv"


mapping={

"CONFLICT_DB_001":
("KEEP_CURRENT","NO_MIGRATION","LOW"),

"CONFLICT_DB_002":
("KEEP_CURRENT","ARCHIVE_LEGACY","MEDIUM"),

"CONFLICT_DB_003":
("HOLD","REVIEW_REQUIRED","HIGH")

}


results=[]


with open(src,"r",encoding="utf-8") as f:

    reader=csv.DictReader(f)

    for row in reader:

        decision,mt,risk=mapping[row["Conflict_ID"]]

        results.append({

        "Migration_ID":"MIGRATION_"+row["Conflict_ID"],

        "Database_A":row["Database_A"],

        "Database_B":row["Database_B"],

        "Decision":decision,

        "Migration_Type":mt,

        "Risk_Level":risk,

        "Approval_Status":"PENDING",

        "Validation_Time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        })


with open(out,"w",newline="",encoding="utf-8") as f:

    writer=csv.DictWriter(
        f,
        fieldnames=[
        "Migration_ID",
        "Database_A",
        "Database_B",
        "Decision",
        "Migration_Type",
        "Risk_Level",
        "Approval_Status",
        "Validation_Time"
        ])

    writer.writeheader()
    writer.writerows(results)


print("Database Migration Decision Completed")
print(out)

