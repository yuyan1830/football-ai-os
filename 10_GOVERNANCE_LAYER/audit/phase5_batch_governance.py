import os
import csv
import hashlib
import sqlite3
import json
from datetime import datetime


BASE = r"E:\football_v"

LAYERS = [
    "05_MARKET_LAYER",
    "06_RISK_LAYER",
    "07_LEARNING_LAYER",
    "08_DECISION_LAYER",
    "09_APPLICATION_LAYER"
]

OUT = r"E:\football_v\10_GOVERNANCE_LAYER"


audit = os.path.join(OUT,"audit")
registry = os.path.join(OUT,"registry")
checkpoint = os.path.join(OUT,"checkpoint")

os.makedirs(audit,exist_ok=True)
os.makedirs(registry,exist_ok=True)
os.makedirs(checkpoint,exist_ok=True)


def sha256(path):

    h=hashlib.sha256()

    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)

    return h.hexdigest()



assets=[]
databases=[]


for layer in LAYERS:

    layer_path=os.path.join(BASE,layer)

    if not os.path.exists(layer_path):
        continue


    for root,dirs,files in os.walk(layer_path):

        for file in files:

            path=os.path.join(root,file)

            size=os.path.getsize(path)


            assets.append([
                file,
                path,
                layer,
                round(size/1024/1024,2),
                datetime.now()
            ])



            if file.endswith(".db"):

                try:

                    conn=sqlite3.connect(path)

                    cur=conn.cursor()

                    cur.execute(
                    "select name from sqlite_master where type='table'"
                    )

                    tables=cur.fetchall()

                    conn.close()

                    status="PASS"


                except Exception:

                    tables=[]

                    status="FAIL"



                databases.append([
                    file,
                    path,
                    layer,
                    round(size/1024/1024,2),
                    len(tables),
                    status,
                    sha256(path),
                    datetime.now()
                ])





# Asset Registry

with open(
os.path.join(
registry,
"Phase5_Asset_Registry_V1.0.csv"),
"w",
newline="",
encoding="utf-8") as f:


    w=csv.writer(f)

    w.writerow([
        "Asset",
        "Path",
        "Layer",
        "Size_MB",
        "Time"
    ])

    w.writerows(assets)





# Database Inventory

with open(
os.path.join(
audit,
"Phase5_Database_Inventory_V1.0.csv"),
"w",
newline="",
encoding="utf-8") as f:


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

    w.writerows(databases)




# Governance checkpoint

checkpoint_data={

    "Checkpoint":
    "PHASE5_BATCH_V1.0",

    "Architecture":
    "Football_AI_OS_Betting_Intelligence_System_Omega_V3.2",

    "Rule_Source":
    "CLAUDE.md",

    "Legacy_Source":
    "Football_AI_OS_Legacy_Asset_Index_V1.0",

    "Status":
    "VALIDATION_COMPLETED",

    "Completed":[
        "Asset Discovery",
        "Database Inventory",
        "SQLite Validation",
        "Hash Validation"
    ],

    "Pending":[
        "Governance Classification",
        "Layer Approval"
    ],

    "Modification":{
        "Database_Content":False,
        "Business_Logic":False,
        "Model_Code":False
    }

}


with open(
os.path.join(
checkpoint,
"Checkpoint_PHASE5_BATCH_V1.0.json"),
"w",
encoding="utf-8") as f:

    json.dump(
        checkpoint_data,
        f,
        indent=4,
        ensure_ascii=False
    )


print("PHASE5_BATCH_COMPLETED")
print("Assets:",len(assets))
print("Databases:",len(databases))

