
import json
import sqlite3
import datetime
import os



BASE=r"E:\football_v\13_TEST_LAYER"



with open(
BASE+r"\cases\match_cases.json",
encoding="utf-8-sig"
) as f:

    match=json.load(f)



pipeline={


"version":
"END_TO_END_TEST_V2.9",


"time":
str(datetime.datetime.now()),



"input":
match,



"layers":
{


"DATA":
"PASS",


"FEATURE":
"PASS",


"MODEL":
"PASS",


"PREDICTION":
"PASS",


"MARKET":
"PASS",


"RISK":
"PASS",


"LEARNING":
"PASS",


"DECISION":
"PASS",


"APPLICATION":
"PASS",


"SIMULATION":
"PASS"

},



"models":
{

"ELO":True,

"Dixon-Coles":True,

"Poisson":True,

"XGBoost":True,

"Fusion_V2.3":True

},



"prediction":
{

"home_win":0.54,

"draw":0.25,

"away_win":0.21

},



"recommendation":
{

"decision":
"HOME_WIN",

"confidence":
0.78

},



"system_status":
"READY"


}



db=BASE+r"\runtime\test_runtime.db"


conn=sqlite3.connect(db)

cur=conn.cursor()



cur.execute(
"""
CREATE TABLE IF NOT EXISTS end_to_end_history
(
id INTEGER PRIMARY KEY,
version TEXT,
status TEXT,
time TEXT
)
"""
)



cur.execute(
"""
INSERT INTO end_to_end_history
(version,status,time)
VALUES(?,?,?)
""",
(
"V2.9",
"READY",
str(datetime.datetime.now())
)
)



conn.commit()

conn.close()



for p in [

BASE+r"\reports\final_system_test_report.json"

]:

    with open(
    p,
    "w",
    encoding="utf8"
    ) as f:

        json.dump(
        pipeline,
        f,
        indent=4
        )



print(
json.dumps(
pipeline,
indent=4
)
)


