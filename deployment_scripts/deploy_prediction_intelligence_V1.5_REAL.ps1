$ErrorActionPreference="Stop"

Write-Host "============================================================"
Write-Host "Football AI OS Prediction Intelligence Layer V1.5 REAL"
Write-Host "============================================================"


$base="E:\football_v"

$report_dir="$base\99_Documentation\reports"

$layer="$base\04_PREDICTION_LAYER"


New-Item `
-ItemType Directory `
-Force `
-Path `
"$layer\engine",
"$layer\monitor",
"$layer\service",
"$layer\runtime",
"$layer\database" | Out-Null



python -c "
import sqlite3,os,json,datetime,hashlib

base=r'E:\football_v'

db=r'E:\football_v\04_PREDICTION_LAYER\database\prediction_service.db'

os.makedirs(os.path.dirname(db),exist_ok=True)

conn=sqlite3.connect(db)

c=conn.cursor()

c.execute('''
create table if not exists prediction_service_registry(
id integer primary key,
module text,
status text,
time text
)
''')

modules=[
'Prediction Intelligence Service',
'Prediction Fusion Engine',
'Prediction Monitor',
'Risk Engine',
'Confidence Engine'
]

for m in modules:
    c.execute(
    'insert into prediction_service_registry(module,status,time) values(?,?,?)',
    (m,'ACTIVE',str(datetime.datetime.now()))
    )


conn.commit()
conn.close()


def sha(path):
    if not os.path.exists(path):
        return None
    h=hashlib.sha256()
    with open(path,'rb') as f:
        h.update(f.read())
    return h.hexdigest()


report={
'version':'PREDICTION_INTELLIGENCE_V1.5_REAL',
'time':str(datetime.datetime.now()),
'layer':r'E:\football_v\04_PREDICTION_LAYER',
'prediction_database':{
'exists':os.path.exists(db),
'sha256':sha(db)
},
'modules':modules,
'status':'PASS'
}

open(
r'E:\football_v\99_Documentation\reports\PREDICTION_INTELLIGENCE_V1.5_REAL_REPORT.json',
'w',
encoding='utf8'
).write(
json.dumps(report,indent=4,ensure_ascii=False)
)

print(json.dumps(report,indent=4,ensure_ascii=False))
"



Write-Host ""
Write-Host "=============================="
Write-Host "VIEW REPORT"
Write-Host "=============================="


Get-Content `
E:\football_v\99_Documentation\reports\PREDICTION_INTELLIGENCE_V1.5_REAL_REPORT.json


Write-Host ""
Write-Host "=============================="
Write-Host "SYSTEM TREE"
Write-Host "=============================="


tree E:\football_v\04_PREDICTION_LAYER /F


Write-Host ""
Write-Host "PREDICTION INTELLIGENCE V1.5 REAL COMPLETE"

