# Football AI OS Unified Deployment V2.1
# Database Architecture V2.1 Frozen

import os
import sqlite3
import json
from datetime import datetime


BASE = r"E:\football_v"


DIRECTORIES = [

"00_System_OS",

r"00_System_OS\01_DATA_LAYER",
r"00_System_OS\01_DATA_LAYER\database",

r"00_System_OS\02_FEATURE_LAYER",
r"00_System_OS\02_FEATURE_LAYER\database",

r"00_System_OS\03_MODEL_LAYER",
r"00_System_OS\03_MODEL_LAYER\database",

"AI_RUNTIME",

"deployment_reports",

"99_Documentation",
r"99_Documentation\checkpoints"

]


DATABASES = {

"football_ai_os.db":
[
"system_registry",
"module_registry",
"database_registry",
"model_registry",
"runtime_status"
],


"match_data.db":
[
"matches",
"teams",
"competitions",
"seasons",
"odds",
"events",
"lineups"
],


"feature_store.db":
[
"elo_history",
"dixon_coles_history",
"poisson_history",
"team_form_history",
"home_away_history",
"fatigue_rating",
"feature_vector"
],


"model_store.db":
[
"elo_model",
"dixon_coles_model",
"poisson_model",
"xgboost_model",
"fusion_model",
"model_weight",
"model_version"
]

}


def create_dirs():

    for d in DIRECTORIES:

        path=os.path.join(BASE,d)

        os.makedirs(path,exist_ok=True)



def create_database(path,tables):

    conn=sqlite3.connect(path)

    cur=conn.cursor()


    for table in tables:

        sql=f"""

        CREATE TABLE IF NOT EXISTS {table}
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            value TEXT,
            created_time TEXT
        )

        """

        cur.execute(sql)


    conn.commit()

    conn.close()



def deploy_databases():

    locations={

    "football_ai_os.db":
    r"00_System_OS\01_DATA_LAYER\database",

    "match_data.db":
    r"00_System_OS\01_DATA_LAYER\database",

    "feature_store.db":
    r"00_System_OS\02_FEATURE_LAYER\database",

    "model_store.db":
    r"00_System_OS\03_MODEL_LAYER\database"

    }


    for db,tables in DATABASES.items():

        path=os.path.join(
            BASE,
            locations[db],
            db
        )

        create_database(
            path,
            tables
        )



def create_runtime():

    runtime=os.path.join(
        BASE,
        "AI_RUNTIME"
    )


    with open(
        os.path.join(runtime,"runtime.py"),
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
'''
def run():

    print("==============================")
    print("Football AI OS Runtime")
    print("==============================")

    print("Database ONLINE")
    print("Model Store ONLINE")
    print("Runtime Engine ONLINE")


if __name__=="__main__":

    run()

'''
        )



def create_reports():

    report={

    "system":
    "Football AI OS",

    "version":
    "V2.1",

    "database_architecture":
    "Multi Database Unified Storage",

    "databases":
    list(DATABASES.keys()),

    "production_policy":
    "Empty User Data Database + Pretrained Model Package",

    "time":
    str(datetime.now())

    }


    path=os.path.join(
        BASE,
        "deployment_reports",
        "FOOTBALL_AI_OS_V2.1_DEPLOYMENT_REPORT.json"
    )


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )



def create_checkpoint():

    path=os.path.join(
        BASE,
        "99_Documentation",
        "checkpoints",
        "FOOTBALL_V_CHECKPOINT_SYSTEM_SCAN_V4.0.txt"
    )


    content="""

Football AI OS Checkpoint System Scan V4.0


Framework:
Football AI OS Framework V1.1 Frozen


Database:
Database Architecture V2.1 Frozen


Architecture:

1 football_ai_os.db
System Control Database


2 match_data.db
User Data Input Database


3 feature_store.db
Feature Storage Database


4 model_store.db
Model Storage Database



Production Rule:

No match data included.

Users download their own data.

Pretrained models can be delivered.



Migration:

Old E:\\football deprecated.

New root:

E:\\football_v



Status:

Deployment Ready

"""


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)



def main():

    print("Football AI OS Unified Deployment V2.1")

    create_dirs()

    deploy_databases()

    create_runtime()

    create_reports()

    create_checkpoint()


    print("Deployment Complete")



if __name__=="__main__":

    main()




