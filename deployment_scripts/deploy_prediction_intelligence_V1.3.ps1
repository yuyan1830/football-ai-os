# Football AI OS Prediction Intelligence Layer V1.3

Write-Host "============================================================"
Write-Host "Football AI OS Prediction Intelligence Layer V1.3"
Write-Host "============================================================"


$root="E:\football_v"

$dirs=@(
"$root\04_PREDICTION_LAYER",
"$root\04_PREDICTION_LAYER\database",
"$root\04_PREDICTION_LAYER\engine",
"$root\04_PREDICTION_LAYER\service",
"$root\04_PREDICTION_LAYER\monitor",
"$root\04_PREDICTION_LAYER\runtime"
)


foreach($d in $dirs){
    if(!(Test-Path $d)){
        New-Item -ItemType Directory -Path $d | Out-Null
    }
}


$db="$root\04_PREDICTION_LAYER\database\prediction_service.db"


python -c "
import sqlite3, json, os, hashlib, datetime

db=r'$db'

conn=sqlite3.connect(db)
c=conn.cursor()


tables={

'prediction_history':
'''
CREATE TABLE IF NOT EXISTS prediction_history(
id INTEGER PRIMARY KEY AUTOINCREMENT,
match_id INTEGER,
prediction TEXT,
probability REAL,
created_time TEXT
)
''',

'probability_fusion':
'''
CREATE TABLE IF NOT EXISTS probability_fusion(
id INTEGER PRIMARY KEY AUTOINCREMENT,
match_id INTEGER,
elo_probability REAL,
dixon_probability REAL,
poisson_probability REAL,
xgboost_probability REAL,
fusion_probability REAL
)
''',

'prediction_result':
'''
CREATE TABLE IF NOT EXISTS prediction_result(
id INTEGER PRIMARY KEY AUTOINCREMENT,
match_id INTEGER,
home_team TEXT,
away_team TEXT,
result TEXT,
confidence REAL,
risk REAL
)
''',

'prediction_audit':
'''
CREATE TABLE IF NOT EXISTS prediction_audit(
id INTEGER PRIMARY KEY AUTOINCREMENT,
module TEXT,
status TEXT,
time TEXT
)
'''

}


for k,v in tables.items():
    c.execute(v)


c.execute(
'''
INSERT INTO prediction_audit
(module,status,time)
VALUES
(?,?,?)
''',
(
'Prediction Intelligence V1.3',
'ACTIVE',
datetime.datetime.now().isoformat()
)
)


conn.commit()

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        h.update(f.read())
    return h.hexdigest()


report={
"version":"PREDICTION_INTELLIGENCE_V1.3",
"time":datetime.datetime.now().isoformat(),
"database":{
"path":db,
"size":os.path.getsize(db),
"sha256":sha256(db),
"tables":[x[0] for x in c.execute(
\"select name from sqlite_master where type='table'\"
).fetchall()]
},
"status":"PASS"
}


os.makedirs(
r'E:\football_v\99_Documentation\reports',
exist_ok=True
)

with open(
r'E:\football_v\99_Documentation\reports\PREDICTION_INTELLIGENCE_V1.3_REPORT.json',
'w',
encoding='utf8'
) as f:
    json.dump(report,f,indent=4,ensure_ascii=False)


print(json.dumps(report,indent=4,ensure_ascii=False))

conn.close()

"

Write-Host ""
Write-Host "=============================="
Write-Host "DATABASE TEST"
Write-Host "=============================="

python -c "
import sqlite3
db=r'E:\football_v\04_PREDICTION_LAYER\database\prediction_service.db'
c=sqlite3.connect(db).cursor()
print(c.execute(
\"select name from sqlite_master where type='table'\"
).fetchall())
"


Write-Host ""
Write-Host "=============================="
Write-Host "VIEW REPORT"
Write-Host "=============================="

Get-Content `
E:\football_v\99_Documentation\reports\PREDICTION_INTELLIGENCE_V1.3_REPORT.json


Write-Host ""
Write-Host "=============================="
Write-Host "SYSTEM TREE"
Write-Host "=============================="

tree `
E:\football_v\04_PREDICTION_LAYER /F


Write-Host ""
Write-Host "PREDICTION INTELLIGENCE V1.3 COMPLETE"

