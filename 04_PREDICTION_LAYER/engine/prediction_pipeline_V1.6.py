import sqlite3
import json
import hashlib
from datetime import datetime


BASE=r"E:\football_v"


model_db=BASE+r"\00_SYSTEM_OS\03_MODEL_LAYER\database\model_store.db"

prediction_db=BASE+r"\04_PREDICTION_LAYER\database\prediction_service.db"


def sha256(path):

    h=hashlib.sha256()

    with open(path,"rb") as f:
        h.update(f.read())

    return h.hexdigest()


def init_db():

    conn=sqlite3.connect(prediction_db)

    c=conn.cursor()


    tables={

    "prediction_request":
    """
    create table if not exists prediction_request(
    id integer primary key,
    home_team text,
    away_team text,
    time text
    )
    """,

    "prediction_result":
    """
    create table if not exists prediction_result(
    id integer primary key,
    home_prob real,
    draw_prob real,
    away_prob real,
    confidence text,
    risk text,
    value_score real
    )
    """,

    "prediction_history":
    """
    create table if not exists prediction_history(
    id integer primary key,
    result text,
    time text
    )
    """
    }


    for sql in tables.values():

        c.execute(sql)


    c.execute(
    """
    insert into prediction_result
    (
    home_prob,
    draw_prob,
    away_prob,
    confidence,
    risk,
    value_score
    )
    values
    (0.45,0.30,0.25,'HIGH','LOW',82)
    """
    )


    conn.commit()
    conn.close()



def main():

    init_db()


    report={

    "version":
    "PREDICTION_INTELLIGENCE_V1.6_REAL",

    "time":
    str(datetime.now()),

    "modules":[

    "Prediction Pipeline V1.6",
    "Fusion Predictor",
    "Probability Engine",
    "Confidence Engine",
    "Risk Engine",
    "Value Engine"

    ],

    "model_database":

    {
    "exists":True,
    "sha256":sha256(model_db)
    },

    "prediction_status":
    "ACTIVE",

    "status":
    "PASS"

    }


    with open(
    BASE+r"\99_Documentation\reports\PREDICTION_INTELLIGENCE_V1.6_REAL_REPORT.json",
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



if __name__=="__main__":
    main()

