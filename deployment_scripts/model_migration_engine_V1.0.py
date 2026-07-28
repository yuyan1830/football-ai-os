import sqlite3
import os
import json
import hashlib
from datetime import datetime


BASE=r"E:\football_v"


MODEL_DB=os.path.join(
BASE,
"00_SYSTEM_OS",
"03_MODEL_LAYER",
"database",
"model_store.db"
)


SYSTEM_DB=os.path.join(
BASE,
"00_SYSTEM_OS",
"01_DATA_LAYER",
"database",
"football_ai_os.db"
)


REPORT=os.path.join(
BASE,
"99_Documentation",
"reports",
"MODEL_MIGRATION_V1.0_REPORT.json"
)



def sha256(path):

    h=hashlib.sha256()

    with open(path,"rb") as f:

        for b in iter(lambda:f.read(8192),b""):

            h.update(b)

    return h.hexdigest()



def upgrade_model_schema():

    conn=sqlite3.connect(MODEL_DB)

    cur=conn.cursor()


    tables={


    "elo_model":
    """
    id INTEGER PRIMARY KEY,
    model_name TEXT,
    version TEXT,
    status TEXT
    """,


    "dixon_coles_model":
    """
    id INTEGER PRIMARY KEY,
    model_name TEXT,
    version TEXT,
    status TEXT
    """,


    "poisson_model":
    """
    id INTEGER PRIMARY KEY,
    model_name TEXT,
    version TEXT,
    status TEXT
    """,


    "xgboost_model":
    """
    id INTEGER PRIMARY KEY,
    model_name TEXT,
    version TEXT,
    status TEXT
    """,


    "fusion_model":
    """
    id INTEGER PRIMARY KEY,
    model_name TEXT,
    version TEXT,
    status TEXT
    """,


    "model_weight":
    """
    id INTEGER PRIMARY KEY,
    model_name TEXT,
    weight REAL
    """,


    "model_version":
    """
    id INTEGER PRIMARY KEY,
    version TEXT,
    release TEXT
    """

    }



    for t,s in tables.items():

        cur.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {t}
        ({s})
        """
        )


    conn.commit()
    conn.close()



def migrate_models():

    conn=sqlite3.connect(MODEL_DB)

    cur=conn.cursor()


    models=[

    "ELO",

    "DIXON_COLES",

    "POISSON",

    "XGBOOST",

    "FUSION"

    ]


    for m in models:

        table=m.lower()+"_model"


        if m=="DIXON_COLES":
            table="dixon_coles_model"

        elif m=="XGBOOST":
            table="xgboost_model"

        elif m=="FUSION":
            table="fusion_model"


        cur.execute(
        f"""
        INSERT INTO {table}
        (model_name,version,status)
        VALUES(?,?,?)
        """,
        (
        m,
        "V2.2",
        "ACTIVE"
        )
        )


    cur.execute(
    """
    INSERT INTO model_weight
    (model_name,weight)
    VALUES
    ('ELO',0.20),
    ('DIXON_COLES',0.20),
    ('POISSON',0.20),
    ('XGBOOST',0.20),
    ('FUSION',0.20)
    """
    )


    cur.execute(
    """
    INSERT INTO model_version
    (version,release)
    VALUES
    ('V2.2','INITIAL_MODEL_RELEASE')
    """
    )


    conn.commit()

    conn.close()



def register_system_model():


    conn=sqlite3.connect(SYSTEM_DB)

    cur=conn.cursor()


    cur.execute(
    """
    PRAGMA table_info(model_registry)
    """
    )


    cols=[
    x[1]
    for x in cur.fetchall()
    ]


    data={}


    if "model_name" in cols:
        data["model_name"]="Football_AI_Fusion"


    if "version" in cols:
        data["version"]="V2.2"


    if "status" in cols:
        data["status"]="ACTIVE"


    if data:


        names=list(data.keys())

        values=[
        data[x]
        for x in names
        ]


        cur.execute(
        f"""
        INSERT INTO model_registry
        ({",".join(names)})
        VALUES
        ({",".join(["?"]*len(values))})
        """,
        values
        )


    conn.commit()

    conn.close()



def check():

    result={}


    for name,path in {

    "model_store":MODEL_DB,

    "system":SYSTEM_DB

    }.items():


        conn=sqlite3.connect(path)

        cur=conn.cursor()


        cur.execute(
        """
        SELECT name FROM sqlite_master
        WHERE type='table'
        """
        )


        result[name]={

        "size":os.path.getsize(path),

        "sha256":sha256(path),

        "tables":[x[0] for x in cur.fetchall()]

        }


        conn.close()


    return result



def main():

    print("="*60)

    print("Football AI OS Model Migration V1.0")

    print("="*60)


    upgrade_model_schema()

    migrate_models()

    register_system_model()


    report={

    "version":
    "MODEL_MIGRATION_V1.0",

    "time":
    datetime.now().isoformat(),

    "result":
    check()

    }


    os.makedirs(
    os.path.dirname(REPORT),
    exist_ok=True
    )


    with open(
    REPORT,
    "w",
    encoding="utf8"
    ) as f:

        json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
        )


    print(json.dumps(
    report,
    indent=4,
    ensure_ascii=False
    ))


    print("MODEL MIGRATION COMPLETE")



if __name__=="__main__":

    main()

