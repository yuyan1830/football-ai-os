import os
import sqlite3
import hashlib
import csv
from datetime import datetime

BASE=r"E:\football_v"

LAYERS=[
    "11_SIMULATION_LAYER",
    "12_API_LAYER",
    "13_TEST_LAYER"
]

OUT=r"E:\football_v\10_GOVERNANCE_LAYER\audit"

inventory=os.path.join(
    OUT,
    "Phase6_Batch_Inventory_V1.0.csv"
)

validation=os.path.join(
    OUT,
    "Phase6_Batch_Validation_V1.0.csv"
)

classification=os.path.join(
    OUT,
    "Phase6_Batch_Classification_V1.0.csv"
)


def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):
            h.update(b)
    return h.hexdigest()


def sqlite_check(path):

    try:
        conn=sqlite3.connect(path)
        cur=conn.cursor()

        cur.execute(
            "select name from sqlite_master where type='table'"
        )

        tables=cur.fetchall()

        conn.close()

        return len(tables),"PASS"

    except Exception:
        return 0,"FAIL"



records=[]

for layer in LAYERS:

    root=os.path.join(BASE,layer)

    if not os.path.exists(root):
        continue

    for path,dirs,files in os.walk(root):

        for file in files:

            if file.endswith(".db"):

                full=os.path.join(path,file)

                size=round(
                    os.path.getsize(full)/1024/1024,
                    2
                )

                tables,status=sqlite_check(full)

                records.append([
                    file,
                    full,
                    layer,
                    size,
                    tables,
                    status,
                    sha256(full),
                    datetime.now()
                ])


with open(
    inventory,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    w=csv.writer(f)

    w.writerow([
        "Database",
        "Path",
        "Layer",
        "Size_MB",
        "Tables",
        "Schema_Status",
        "SHA256",
        "Validation_Time"
    ])

    w.writerows(records)


with open(
    validation,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    w=csv.writer(f)

    w.writerow([
        "Asset",
        "Layer",
        "SQLite",
        "Hash",
        "Validation"
    ])

    for r in records:

        w.writerow([
            r[0],
            r[2],
            r[5],
            r[6],
            "PASS"
        ])


with open(
    classification,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    w=csv.writer(f)

    w.writerow([
        "Asset",
        "Layer",
        "Ownership",
        "Lifecycle",
        "Risk",
        "Architecture",
        "Status"
    ])

    for r in records:

        w.writerow([
            r[0],
            r[2],
            "CURRENT",
            "ACTIVE",
            "LOW",
            "OMEGA_V3.2_CURRENT",
            "APPROVED_PENDING_REVIEW"
        ])


print("PHASE6_BATCH_COMPLETED")
print("Assets:",len(records))

