import csv
import os
import sqlite3
from datetime import datetime


registry_files = [
    r"E:\football_v\10_GOVERNANCE_LAYER\registry\Database_Registry.csv",
    r"E:\football_v\10_GOVERNANCE_LAYER\registry\Database_Inventory.csv"
]


src = None

for f in registry_files:
    if os.path.exists(f):
        src = f
        break


if src is None:
    raise FileNotFoundError("No database registry csv found")


output = r"E:\football_v\10_GOVERNANCE_LAYER\audit\Database_Schema_Validation.csv"


results=[]


with open(src,"r",encoding="utf-8-sig") as f:

    reader=csv.DictReader(f)

    for index,row in enumerate(reader,1):

        path = row.get("Path")

        if path is None:
            path=row.get("FullName")


        if not path:
            continue


        result={
            "Database_ID":row.get("Database_ID",f"DB{index:04d}"),
            "Database_Name":row.get("Database_Name",os.path.basename(path)),
            "Path":path,
            "Exists":False,
            "Tables":0,
            "Schema_Status":"FAILED",
            "Validation_Time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


        if os.path.exists(path):

            result["Exists"]=True

            try:

                conn=sqlite3.connect(path)

                cur=conn.cursor()

                cur.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                )

                tables=cur.fetchall()

                result["Tables"]=len(tables)

                result["Schema_Status"]="PASS"


                conn.close()


            except Exception as e:

                result["Schema_Status"]="ERROR"


        results.append(result)



with open(output,"w",newline="",encoding="utf-8-sig") as f:

    writer=csv.DictWriter(
        f,
        fieldnames=[
            "Database_ID",
            "Database_Name",
            "Path",
            "Exists",
            "Tables",
            "Schema_Status",
            "Validation_Time"
        ]
    )

    writer.writeheader()

    writer.writerows(results)



print("Database Schema Validation Completed")
print(output)

