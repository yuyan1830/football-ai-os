import sqlite3
import csv
import os
from datetime import datetime


pairs = [
(
"CONFLICT_DB_001",
r"E:\football_v\01_DATA_LAYER\database\match_data.db",
r"E:\football_v\00_System_OS\01_DATA_LAYER\database\match_data.db"
),
(
"CONFLICT_DB_002",
r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db",
r"E:\football_v\00_System_OS\02_FEATURE_LAYER\database\feature_store.db"
),
(
"CONFLICT_DB_003",
r"E:\football_v\03_MODEL_LAYER\database\model_store.db",
r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"
)
]


out=r"E:\football_v\10_GOVERNANCE_LAYER\audit\Database_Table_Comparison_V1.0.csv"


def get_tables(path):

    conn=sqlite3.connect(path)
    cur=conn.cursor()

    tables=[
        x[0]
        for x in cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
        )
    ]

    result={}

    for t in tables:

        cols=cur.execute(
            f"PRAGMA table_info('{t}')"
        ).fetchall()

        count=cur.execute(
            f"SELECT COUNT(*) FROM '{t}'"
        ).fetchone()[0]


        pk=[
            c[1]
            for c in cols
            if c[5]==1
        ]


        result[t]={
            "columns":len(cols),
            "records":count,
            "primary_key":",".join(pk)
        }


    conn.close()

    return result



rows=[]


for cid,a,b in pairs:

    ta=get_tables(a)
    tb=get_tables(b)


    all_tables=sorted(
        set(ta.keys()) |
        set(tb.keys())
    )


    for table in all_tables:

        rows.append(
        {
        "Conflict_ID":cid,
        "Table_Name":table,

        "A_Exists":table in ta,
        "B_Exists":table in tb,

        "A_Columns":
            ta.get(table,{}).get("columns",""),

        "B_Columns":
            tb.get(table,{}).get("columns",""),

        "A_Records":
            ta.get(table,{}).get("records",""),

        "B_Records":
            tb.get(table,{}).get("records",""),

        "A_Primary_Key":
            ta.get(table,{}).get("primary_key",""),

        "B_Primary_Key":
            tb.get(table,{}).get("primary_key",""),

        "Validation_Time":
            datetime.now()

        }
        )



os.makedirs(
    os.path.dirname(out),
    exist_ok=True
)


with open(
    out,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer=csv.DictWriter(
        f,
        fieldnames=rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(rows)


print("Database Table Comparison Completed")
print(out)

