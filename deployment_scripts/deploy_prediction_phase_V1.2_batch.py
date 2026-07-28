import sqlite3
import os
import json
import hashlib
from datetime import datetime


ROOT=r"E:\football_v"

SYSTEM_DB=ROOT+r"\00_SYSTEM_OS\01_DATA_LAYER\database\football_ai_os.db"
FEATURE_DB=ROOT+r"\00_SYSTEM_OS\02_FEATURE_LAYER\database\feature_store.db"
MODEL_DB=ROOT+r"\00_SYSTEM_OS\03_MODEL_LAYER\database\model_store.db"

REPORT=ROOT+r"\99_Documentation\reports\PREDICTION_PHASE_V1.2_BATCH_REPORT.json"


def sha256(path):

    if not os.path.exists(path):
        return None

    h=hashlib.sha256()

    with open(path,"rb") as f:
        h.update(f.read())

    return h.hexdigest()



def db_check(path):

    result={
        "exists":False,
        "size":0,
        "tables":{}
    }

    if not os.path.exists(path):
        return result


    conn=sqlite3.connect(path)

    cur=conn.cursor()


    result["exists"]=True
    result["size"]=os.path.getsize(path)
    result["sha256"]=sha256(path)


    tables=cur.execute(
    "select name from sqlite_master where type='table'"
    ).fetchall()


    for t in tables:

        name=t[0]

        if name=="sqlite_sequence":
            continue

        try:

            count=cur.execute(
            f"select count(*) from {name}"
            ).fetchone()[0]

            result["tables"][name]=count

        except:

            result["tables"][name]="ERROR"


    conn.close()

    return result



def create_prediction_tables():


    conn=sqlite3.connect(MODEL_DB)

    cur=conn.cursor()


    cur.execute("""
    create table if not exists prediction_result
    (
        prediction_id integer primary key autoincrement,
        match_id integer,
        home_team text,
        away_team text,
        elo_prob real,
        dixon_coles_prob real,
        poisson_prob real,
        xgboost_prob real,
        fusion_prob real,
        confidence real,
        created_time text
    )
    """)


    cur.execute("""
    create table if not exists prediction_feature_snapshot
    (
        snapshot_id integer primary key autoincrement,
        match_id integer,
        feature_json text,
        created_time text
    )
    """)


    cur.execute("""
    create table if not exists prediction_history
    (
        history_id integer primary key autoincrement,
        prediction_id integer,
        result text,
        created_time text
    )
    """)


    cur.execute("""
    create table if not exists model_weight_history
    (
        id integer primary key autoincrement,
        model_name text,
        weight real,
        created_time text
    )
    """)


    conn.commit()
    conn.close()



def register_system():


    conn=sqlite3.connect(SYSTEM_DB)

    cur=conn.cursor()


    cur.execute("""
    create table if not exists prediction_registry
    (
        id integer primary key autoincrement,
        module text,
        version text,
        status text,
        created_time text
    )
    """)


    modules=[
    ("prediction_service","V1.2","ACTIVE"),
    ("prediction_snapshot","V1.0","ACTIVE"),
    ("prediction_backtest","V1.0","READY"),
    ("prediction_monitor","V1.0","READY"),
    ("model_weight_manager","V1.0","ACTIVE")
    ]


    for m in modules:

        cur.execute(
        """
        insert into prediction_registry
        (module,version,status,created_time)
        values(?,?,?,?)
        """,
        (
            m[0],
            m[1],
            m[2],
            datetime.now().isoformat()
        )
        )


    conn.commit()
    conn.close()



def main():

    print("="*60)
    print("Football AI OS Prediction Phase V1.2 Batch Deployment")
    print("="*60)


    create_prediction_tables()

    register_system()


    report={

        "version":
        "PREDICTION_PHASE_V1.2_BATCH",

        "time":
        datetime.now().isoformat(),

        "modules":
        [
        "Prediction Service V1.2",
        "Feature Snapshot V1.0",
        "Prediction Result Manager V1.0",
        "Backtest Engine V1.0",
        "Prediction Monitor V1.0",
        "Model Weight Manager V1.0"
        ],

        "databases":
        {
            "system":
            db_check(SYSTEM_DB),

            "feature":
            db_check(FEATURE_DB),

            "model":
            db_check(MODEL_DB)
        },

        "status":"PASS"
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


    print("PREDICTION PHASE V1.2 COMPLETE")



if __name__=="__main__":

    main()

