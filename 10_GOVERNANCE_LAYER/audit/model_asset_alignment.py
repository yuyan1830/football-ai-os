import csv
import os
import sqlite3
from datetime import datetime


base=r"E:\football_v"

current=r"E:\football_v\03_MODEL_LAYER\database\model_store.db"
legacy=r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"


out=r"E:\football_v\10_GOVERNANCE_LAYER\audit\Model_Asset_Alignment_Report_V1.0.csv"


def inspect(db):

    if not os.path.exists(db):
        return {}

    conn=sqlite3.connect(db)

    tables={}

    for t in conn.execute(
        "select name from sqlite_master where type='table'"
    ):
        name=t[0]

        count=conn.execute(
            f"select count(*) from '{name}'"
        ).fetchone()[0]

        cols=len(
            conn.execute(
                f"pragma table_info('{name}')"
            ).fetchall()
        )

        tables[name]={
            "columns":cols,
            "records":count
        }

    conn.close()

    return tables



c=inspect(current)
l=inspect(legacy)


rows=[]


for table in sorted(set(c.keys())|set(l.keys())):

    if table in c and table in l:
        status="BOTH_EXIST"
    elif table in c:
        status="CURRENT_ONLY"
    else:
        status="LEGACY_ONLY"


    rows.append({
        "Table_Name":table,
        "Current_Exists":table in c,
        "Legacy_Exists":table in l,
        "Current_Columns":c.get(table,{}).get("columns",""),
        "Legacy_Columns":l.get(table,{}).get("columns",""),
        "Current_Records":c.get(table,{}).get("records",""),
        "Legacy_Records":l.get(table,{}).get("records",""),
        "Asset_Status":status,
        "Decision":"PENDING",
        "Validation_Time":datetime.now()
    })


with open(out,"w",newline="",encoding="utf-8") as f:

    writer=csv.DictWriter(
        f,
        fieldnames=rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(rows)


print("MODEL ASSET ALIGNMENT COMPLETE")
print(out)
