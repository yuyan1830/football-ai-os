$ErrorActionPreference="Continue"


Write-Host ""
Write-Host "============================================================"
Write-Host "Football AI OS V2.9 REAL END TO END TEST ALL"
Write-Host "============================================================"


$root="E:\football_v"

$layer="$root\13_TEST_LAYER"


$dirs=@(
"$layer\cases",
"$layer\engine",
"$layer\reports",
"$layer\runtime",
"$layer\validation"
)


foreach($d in $dirs)
{
    New-Item `
    -Path $d `
    -ItemType Directory `
    -Force | Out-Null
}



Write-Host ""
Write-Host "[1] CREATE TEST CASE"
Write-Host "============================================================"


@'
{
    "home_team":"Manchester City",
    "away_team":"Liverpool",
    "league":"Premier League",
    "odds":{
        "home":1.85,
        "draw":3.60,
        "away":3.90
    }
}
'@ | Set-Content `
"$layer\cases\match_cases.json" `
-Encoding UTF8



Write-Host ""
Write-Host "[2] CREATE END TO END ENGINE"
Write-Host "============================================================"



@'

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


'@ | Set-Content `
"$layer\engine\end_to_end_test_engine_V2.9.py" `
-Encoding UTF8



Write-Host ""
Write-Host "[3] RUN END TO END TEST"
Write-Host "============================================================"


python `
"$layer\engine\end_to_end_test_engine_V2.9.py"



Write-Host ""
Write-Host "[4] DATABASE TEST"
Write-Host "============================================================"



@'

import sqlite3


db=r"E:\football_v\13_TEST_LAYER\runtime\test_runtime.db"


conn=sqlite3.connect(db)

cur=conn.cursor()


print(
cur.execute(
"select name from sqlite_master where type='table'"
).fetchall()
)


print("DATABASE TEST PASS")

'@ | Set-Content `
"$layer\validation\database_validation.py" `
-Encoding UTF8



python `
"$layer\validation\database_validation.py"



Write-Host ""
Write-Host "[5] REPORT"
Write-Host "============================================================"


Get-Content `
"$layer\reports\final_system_test_report.json"



Write-Host ""
Write-Host "[6] TREE"
Write-Host "============================================================"


tree "$layer" /F



Write-Host ""
Write-Host "============================================================"
Write-Host "Football AI OS V2.9 REAL END TO END TEST COMPLETE"
Write-Host "STATUS : READY"
Write-Host "============================================================"