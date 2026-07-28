import csv
from datetime import datetime
import os


src = r"E:\football_v\10_GOVERNANCE_LAYER\audit\Database_SQLite_Comparison_V1.0.csv"

out = r"E:\football_v\10_GOVERNANCE_LAYER\audit\Database_Asset_Classification_V1.0.csv"


if not os.path.exists(src):
    raise FileNotFoundError(src)


results=[]


with open(src,"r",encoding="utf-8") as f:

    reader=csv.DictReader(f)

    for row in reader:

        conflict=row["Conflict_ID"]

        if conflict=="CONFLICT_DB_001":

            status="CORE_CURRENT"
            decision="Keep Omega V3.2 DATA_LAYER match_data.db as primary. Legacy retained."

        elif conflict=="CONFLICT_DB_002":

            status="CORE_CURRENT"
            decision="Keep Omega V3.2 FEATURE_LAYER feature_store.db. Legacy feature assets archived."

        elif conflict=="CONFLICT_DB_003":

            status="MERGE_REQUIRED"
            decision="Preserve Legacy model runtime assets. Review migration after model governance."

        else:

            status="UNKNOWN"
            decision="Manual review required"


        results.append({

            "Conflict_ID":conflict,
            "Database_A":row["Database_A"],
            "Database_B":row["Database_B"],
            "Asset_Status":status,
            "Decision":decision,
            "Validation_Time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        })


with open(out,"w",newline="",encoding="utf-8") as f:

    writer=csv.DictWriter(
        f,
        fieldnames=[
            "Conflict_ID",
            "Database_A",
            "Database_B",
            "Asset_Status",
            "Decision",
            "Validation_Time"
        ]
    )

    writer.writeheader()
    writer.writerows(results)


print("Database Asset Classification Completed")
print(out)
