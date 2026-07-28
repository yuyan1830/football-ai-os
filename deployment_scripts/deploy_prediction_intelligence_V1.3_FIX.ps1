$py="E:\football_v\deployment_scripts\prediction_intelligence_init_V1.3.py"


@"
import sqlite3
import json
import os
import hashlib
import datetime


db=r"E:\football_v\04_PREDICTION_LAYER\database\prediction_service.db"


os.makedirs(
r"E:\football_v\04_PREDICTION_LAYER\database",
exist_ok=True
)


conn=sqlite3.connect(db)

c=conn.cursor()


tables={

"prediction_history":
"""
CREATE TABLE IF NOT EXISTS prediction_history(
id INTEGER PRIMARY KEY AUTOINCREMENT,
match_id INTEGER,
prediction TEXT,
probability REAL,
created_time TEXT
)
""",

"probability_fusion":
"""
CREATE TABLE IF NOT EXISTS probability_fusion(
id INTEGER PRIMARY KEY AUTOINCREMENT,
match_id INTEGER,
elo_probability REAL,
dixon_probability REAL,
poisson_probability REAL,
xgboost_probability REAL,
fusion_probability REAL
)
""",

"prediction_result":
"""
CREATE TABLE IF NOT EXISTS prediction_result(
id INTEGER PRIMARY KEY AUTOINCREMENT,
match_id INTEGER,
home_team TEXT,
away_team TEXT,
result TEXT,
confidence REAL,
risk REAL
)
""",

"prediction_audit":
"""
CREATE TABLE IF NOT EXISTS prediction_audit(
id INTEGER PRIMARY KEY AUTOINCREMENT,
module TEXT,
status TEXT,
time TEXT
)
"""

}


for name,sql in tables.items():
    c.execute(sql)


c.execute(
"""
INSERT INTO prediction_audit
(module,status,time)
VALUES(?,?,?)
""",
(
"Prediction Intelligence V1.3",
"ACTIVE",
datetime.datetime.now().isoformat()
)
)


conn.commit()


def sha256(path):

    h=hashlib.sha256()

    with open(path,"rb") as f:
        h.update(f.read())

    return h.hexdigest()



report={

"version":
"PREDICTION_INTELLIGENCE_V1.3",

"time":
datetime.datetime.now().isoformat(),

"database":
{
"path":db,

"size":os.path.getsize(db),

"sha256":sha256(db),

"tables":
[
x[0]
for x in c.execute(
"SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()
]

},

"status":
"PASS"

}



os.makedirs(
r"E:\football_v\99_Documentation\reports",
exist_ok=True
)



with open(
r"E:\football_v\99_Documentation\reports\PREDICTION_INTELLIGENCE_V1.3_REPORT.json",
"w",
encoding="utf8"
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



conn.close()

"@ | Set-Content $py -Encoding UTF8


python $py


Write-Host ""

Write-Host "=============================="
Write-Host "DATABASE TEST"
Write-Host "=============================="


python - <<PY
