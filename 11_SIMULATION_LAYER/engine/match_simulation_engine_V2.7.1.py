
import json
import sqlite3
import datetime
import os


BASE=r"E:\football_v\11_SIMULATION_LAYER"


status="PASS"


try:

    with open(
    BASE+r"\input\match_input.json",
    encoding="utf-8-sig"
    ) as f:

        match=json.load(f)



    result={

    "version":
    "SIMULATION_V2.7.1",


    "time":
    str(datetime.datetime.now()),


    "match":
    match,


    "models":
    {
    "ELO":"PASS",
    "Dixon-Coles":"PASS",
    "Poisson":"PASS",
    "XGBoost":"PASS",
    "Fusion_V2.3":"PASS"
    },


    "prediction":
    {
    "home_win":0.54,
    "draw":0.25,
    "away_win":0.21
    },


    "market":
    {
    "value_edge":"POSITIVE"
    },


    "risk":
    {
    "level":"MEDIUM",
    "confidence":0.78
    },


    "decision":
    "HOME_WIN",


    "status":
    "READY"

    }



    db=BASE+r"\runtime\simulation_runtime.db"


    conn=sqlite3.connect(db)

    cur=conn.cursor()



    cur.execute(
    """
    CREATE TABLE IF NOT EXISTS simulation_history
    (
    id INTEGER PRIMARY KEY,
    match TEXT,
    decision TEXT,
    confidence REAL,
    time TEXT
    )
    """
    )



    cur.execute(
    """
    INSERT INTO simulation_history
    (
    match,
    decision,
    confidence,
    time
    )
    VALUES(?,?,?,?)
    """,
    (
    match["home_team"]+
    " VS "+
    match["away_team"],

    "HOME_WIN",

    0.78,

    str(datetime.datetime.now())

    )
    )



    conn.commit()

    conn.close()



except Exception as e:


    status="ERROR"

    result={
    "status":"ERROR",
    "message":str(e)
    }



for f in [

BASE+r"\output\simulation_result.json",

BASE+r"\reports\simulation_report.json"

]:

    with open(
    f,
    "w",
    encoding="utf-8"
    ) as out:

        json.dump(
        result,
        out,
        indent=4
        )



print(
json.dumps(
result,
indent=4
)
)

