import sqlite3
import csv
import os
from datetime import datetime


current=r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db"
legacy=r"E:\football_v\00_System_OS\02_FEATURE_LAYER\database\feature_store.db"

out=r"E:\football_v\10_GOVERNANCE_LAYER\audit\Feature_Asset_Alignment_Report_V1.0.csv"


def inspect(path):

    result={}

    if not os.path.exists(path):
        return result

    conn=sqlite3.connect(path)

    tables=conn.execute(
        "select name from sqlite_master where type='table'"
    ).fetchall()

    for t in tables:

        name=t[0]

        cols=conn.execute(
            f"pragma table_info('{name}')"
        ).fetchall()

        count=conn.execute(
            f"select count(*) from '{name}'"
        ).fetchone()[0]


        result[name]={
            "columns":len(cols),
            "records":count
        }


    conn.close()

    return result



c=inspect(current)
l=inspect(legacy)

rows=[]


for name in sorted(set(c)|set(l)):

    if name in c and name in l:
        status="BOTH_EXIST"
    elif name in c:
        status="CURRENT_ONLY"
    else:
        status="LEGACY_ONLY"


    rows.append({

        "Table_Name":name,

        "Current_Exists":name in c,

        "Legacy_Exists":name in l,

        "Current_Columns":c.get(name,{}).get("columns",""),

        "Legacy_Columns":l.get(name,{}).get("columns",""),

        "Current_Records":c.get(name,{}).get("records",""),

        "Legacy_Records":l.get(name,{}).get("records",""),

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


print("FEATURE ASSET ALIGNMENT COMPLETE")
print(out)

