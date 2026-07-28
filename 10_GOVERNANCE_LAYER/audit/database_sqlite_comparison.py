import sqlite3
import csv
import os
from datetime import datetime


pairs = [
(
r"E:\football_v\01_DATA_LAYER\database\match_data.db",
r"E:\football_v\00_System_OS\01_DATA_LAYER\database\match_data.db",
"CONFLICT_DB_001"
),
(
r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db",
r"E:\football_v\00_System_OS\02_FEATURE_LAYER\database\feature_store.db",
"CONFLICT_DB_002"
),
(
r"E:\football_v\03_MODEL_LAYER\database\model_store.db",
r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db",
"CONFLICT_DB_003"
)
]


out=r"E:\football_v\10_GOVERNANCE_LAYER\audit\Database_SQLite_Comparison_V1.0.csv"


def inspect_db(path):

    if not os.path.exists(path):
        return {
            "error":"FILE_NOT_FOUND",
            "path":path
        }

    conn=sqlite3.connect(path)
    cur=conn.cursor()

    tables=cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()

    result=[]

    for t in tables:

        name=t[0]

        cols=cur.execute(
            f"PRAGMA table_info('{name}')"
        ).fetchall()

        count=cur.execute(
            f"SELECT COUNT(*) FROM '{name}'"
        ).fetchone()[0]

        result.append(
            {
            "table":name,
            "columns":len(cols),
            "records":count
            }
        )

    conn.close()

    return result



rows=[]


for a,b,cid in pairs:

    sa=inspect_db(a)
    sb=inspect_db(b)

    rows.append(
    {
    "Conflict_ID":cid,
    "Database_A":a,
    "Database_B":b,
    "Exists_A":os.path.exists(a),
    "Exists_B":os.path.exists(b),
    "Tables_A":len(sa) if isinstance(sa,list) else 0,
    "Tables_B":len(sb) if isinstance(sb,list) else 0,
    "Schema_Compare":
        "MATCH" if sa==sb else "DIFFERENT",
    "Validation_Time":datetime.now()
    }
    )


os.makedirs(
os.path.dirname(out),
exist_ok=True
)


with open(out,"w",newline="",encoding="utf-8") as f:

    writer=csv.DictWriter(
        f,
        fieldnames=rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(rows)


print("SQLite Comparison Completed")
print(out)

