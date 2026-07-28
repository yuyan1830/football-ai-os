# Football AI OS Feature Model Deployment V1.0

import os
import sqlite3
import json
import hashlib
from datetime import datetime


BASE = r"E:\football_v"


DBS = {
    "system":
    os.path.join(
        BASE,
        "00_SYSTEM_OS",
        "01_DATA_LAYER",
        "database",
        "football_ai_os.db"
    ),

    "match":
    os.path.join(
        BASE,
        "00_SYSTEM_OS",
        "01_DATA_LAYER",
        "database",
        "match_data.db"
    ),

    "feature":
    os.path.join(
        BASE,
        "00_SYSTEM_OS",
        "02_FEATURE_LAYER",
        "database",
        "feature_store.db"
    ),

    "model":
    os.path.join(
        BASE,
        "00_SYSTEM_OS",
        "03_MODEL_LAYER",
        "database",
        "model_store.db"
    )
}


REPORT = os.path.join(
    BASE,
    "99_Documentation",
    "reports",
    "FEATURE_MODEL_DEPLOYMENT_V1.0_REPORT.json"
)


def sha256(path):

    h = hashlib.sha256()

    with open(path,"rb") as f:
        for b in iter(lambda:f.read(8192),b""):
            h.update(b)

    return h.hexdigest()



def init_feature():

    path = DBS["feature"]

    os.makedirs(
        os.path.dirname(path),
        exist_ok=True
    )

    conn = sqlite3.connect(path)

    cur = conn.cursor()


    tables = [

        "elo_history",
        "dixon_coles_history",
        "poisson_history",
        "team_form_history",
        "home_away_history",
        "fatigue_rating",
        "feature_vector"

    ]


    for t in tables:

        cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {t}
            (
            id INTEGER PRIMARY KEY
            )
            """
        )


    conn.commit()
    conn.close()



def init_model():

    path = DBS["model"]

    conn = sqlite3.connect(path)

    cur = conn.cursor()


    tables=[

        "elo_model",
        "dixon_coles_model",
        "poisson_model",
        "xgboost_model",
        "fusion_model",
        "model_weight",
        "model_version"

    ]


    for t in tables:

        cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {t}
            (
            id INTEGER PRIMARY KEY
            )
            """
        )


    conn.commit()
    conn.close()




def register_database():

    path = DBS["system"]

    conn = sqlite3.connect(path)

    cur = conn.cursor()


    cur.execute(
        """
        PRAGMA table_info(database_registry)
        """
    )

    columns = cur.fetchall()


    if not columns:

        print("database_registry missing")
        conn.close()
        return


    column_names=[
        c[1] for c in columns
    ]


    for k,v in DBS.items():

        values={}


        if "name" in column_names:
            values["name"]=k

        if "database_name" in column_names:
            values["database_name"]=k

        if "path" in column_names:
            values["path"]=v

        if "db_path" in column_names:
            values["db_path"]=v

        if "version" in column_names:
            values["version"]="V2.2"

        if "status" in column_names:
            values["status"]="ACTIVE"


        cols=list(values.keys())

        vals=[
            values[x]
            for x in cols
        ]


        placeholders=",".join(
            ["?"]*len(vals)
        )


        cur.execute(
            f"""
            INSERT INTO database_registry
            ({",".join(cols)})
            VALUES
            ({placeholders})
            """,
            vals
        )


    conn.commit()

    conn.close()


def check_db(path):

    if not os.path.exists(path):

        return {
            "exists":False
        }


    conn=sqlite3.connect(path)

    cur=conn.cursor()

    cur.execute(
        """
        SELECT name FROM sqlite_master
        WHERE type='table'
        """
    )

    tables=[
        x[0] for x in cur.fetchall()
    ]

    conn.close()


    return {

        "exists":True,
        "size":os.path.getsize(path),
        "sha256":sha256(path),
        "tables":tables

    }



def main():

    print("="*60)

    print(
    "Football AI OS Feature Model Deployment V1.0"
    )

    print("="*60)


    init_feature()

    init_model()

    register_database()


    report={

    "version":
    "FEATURE_MODEL_DEPLOYMENT_V1.0",

    "time":
    datetime.now().isoformat(),

    "databases":{}

    }


    for k,v in DBS.items():

        report["databases"][k]=check_db(v)


    os.makedirs(
        os.path.dirname(REPORT),
        exist_ok=True
    )


    with open(
        REPORT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
        )


    print(
    json.dumps(
    report,
    indent=4,
    ensure_ascii=False
    )
    )


    print("DEPLOYMENT COMPLETE")



if __name__=="__main__":

    main()

