import sqlite3
import csv
import os
from datetime import datetime

db_a = r"E:\football_v\03_MODEL_LAYER\database\model_store.db"
db_b = r"E:\football_v\00_System_OS\03_MODEL_LAYER\database\model_store.db"

out = r"E:\football_v\10_GOVERNANCE_LAYER\audit\Model_Store_Deep_Comparison_V1.0.csv"


def inspect_db(path):

    result = {}

    if not os.path.exists(path):
        return result

    conn = sqlite3.connect(path)
    cur = conn.cursor()

    tables = cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()

    for t in tables:
        name=t[0]

        cols = cur.execute(
            f"PRAGMA table_info('{name}')"
        ).fetchall()

        count = cur.execute(
            f"SELECT COUNT(*) FROM '{name}'"
        ).fetchone()[0]

        result[name]={
            "columns":len(cols),
            "records":count
        }

    conn.close()

    return result


a = inspect_db(db_a)
b = inspect_db(db_b)


all_tables = sorted(
    set(list(a.keys())+list(b.keys()))
)


rows=[]


for table in all_tables:

    rows.append({

        "Table_Name":table,

        "Current_Model_Store_Exists":
            table in a,

        "Legacy_Model_Store_Exists":
            table in b,

        "Current_Columns":
            a.get(table,{}).get("columns",""),

        "Legacy_Columns":
            b.get(table,{}).get("columns",""),

        "Current_Records":
            a.get(table,{}).get("records",""),

        "Legacy_Records":
            b.get(table,{}).get("records",""),

        "Asset_Status":
            (
                "SAME"
                if table in a and table in b
                else
                "LEGACY_ONLY"
                if table not in a
                else
                "CURRENT_ONLY"
            ),

        "Validation_Time":
            datetime.now()

    })


os.makedirs(
    os.path.dirname(out),
    exist_ok=True
)


with open(
    out,
    "w",
    newline="",
    encoding="utf-8-sig"
) as f:

    writer=csv.DictWriter(
        f,
        fieldnames=rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(rows)


print("Model Store Deep Comparison Completed")
print(out)

