# ============================================================
# Football AI OS Prediction Phase V1.2 Fix Deployment
# Version: V1.2.1
# ============================================================

$ErrorActionPreference="Stop"

$ROOT="E:\football_v"

$SYSTEM_DB="$ROOT\00_SYSTEM_OS\01_DATA_LAYER\database\football_ai_os.db"

$DEPLOY="$ROOT\deployment_scripts\deploy_prediction_phase_V1.2_batch.py"

$REPORT_DIR="$ROOT\99_Documentation\reports"

$BACKUP_DIR="$ROOT\99_Documentation\checkpoints"


Write-Host ""
Write-Host "============================================================"
Write-Host "Football AI OS Prediction Phase V1.2 FIX"
Write-Host "============================================================"


# ------------------------------------------------------------
# 1. Backup
# ------------------------------------------------------------

$time=Get-Date -Format "yyyyMMdd_HHmmss"

$backup="$BACKUP_DIR\archive_system_before_prediction_v12_$time.db"


Write-Host ""
Write-Host "[1] Backup System Database"

python -c "
import sqlite3
src=r'$SYSTEM_DB'
dst=r'$backup'
s=sqlite3.connect(src)
b=sqlite3.connect(dst)
s.backup(b)
b.close()
s.close()
print('BACKUP COMPLETE')
"


# ------------------------------------------------------------
# 2. Upgrade prediction_registry schema
# ------------------------------------------------------------


Write-Host ""
Write-Host "[2] Upgrade prediction_registry schema"


python -c "

import sqlite3

db=r'$SYSTEM_DB'

conn=sqlite3.connect(db)

cur=conn.cursor()


cur.execute('''
CREATE TABLE IF NOT EXISTS prediction_registry
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
module TEXT,
version TEXT,
status TEXT,
database_name TEXT,
created_time TEXT
)
''')


cols=[
('module','TEXT'),
('version','TEXT'),
('status','TEXT'),
('database_name','TEXT'),
('created_time','TEXT')
]


existing=[
x[1] for x in cur.execute(
'PRAGMA table_info(prediction_registry)'
).fetchall()
]


for name,typ in cols:

    if name not in existing:

        cur.execute(
        f'ALTER TABLE prediction_registry ADD COLUMN {name} {typ}'
        )

        print('ADD',name)


conn.commit()
conn.close()

print('SCHEMA FIX COMPLETE')

"


# ------------------------------------------------------------
# 3. Run Prediction Phase V1.2
# ------------------------------------------------------------


Write-Host ""
Write-Host "[3] Deploy Prediction Phase V1.2"


python $DEPLOY


if($LASTEXITCODE -ne 0){

Write-Host "Prediction Deployment Failed"

exit 1

}



# ------------------------------------------------------------
# 4. Database Validation
# ------------------------------------------------------------


Write-Host ""
Write-Host "[4] Database Validation"

python -c "

import sqlite3, json, hashlib, os


dbs={

'system':
r'$ROOT\00_SYSTEM_OS\01_DATA_LAYER\database\football_ai_os.db',

'match':
r'$ROOT\00_SYSTEM_OS\01_DATA_LAYER\database\match_data.db',

'feature':
r'$ROOT\00_SYSTEM_OS\02_FEATURE_LAYER\database\feature_store.db',

'model':
r'$ROOT\00_SYSTEM_OS\03_MODEL_LAYER\database\model_store.db'

}


result={}


for n,p in dbs.items():

    data={}

    data['exists']=os.path.exists(p)

    if data['exists']:

        data['size']=os.path.getsize(p)

        h=hashlib.sha256()

        with open(p,'rb') as f:

            h.update(f.read())

        data['sha256']=h.hexdigest()


        c=sqlite3.connect(p).cursor()

        tables=c.execute(
        \"select name from sqlite_master where type='table'\"
        ).fetchall()

        data['tables']={}


        for t in tables:

            name=t[0]

            if name!='sqlite_sequence':

                try:

                    data['tables'][name]=c.execute(
                    f'select count(*) from {name}'
                    ).fetchone()[0]

                except:

                    pass


    result[n]=data



report={

'version':
'DATABASE_VALIDATION_AFTER_PREDICTION_PHASE_V1.2',

'databases':
result

}


out=r'$REPORT_DIR\PREDICTION_PHASE_V1.2_DATABASE_REPORT.json'


with open(out,'w',encoding='utf8') as f:

    json.dump(report,f,indent=4,ensure_ascii=False)


print(json.dumps(report,indent=4))

"


# ------------------------------------------------------------
# 5. Show Report
# ------------------------------------------------------------


Write-Host ""
Write-Host "[5] VIEW REPORT"

Get-Content `
"$REPORT_DIR\PREDICTION_PHASE_V1.2_DATABASE_REPORT.json"


Write-Host ""
Write-Host "============================================================"
Write-Host "Prediction Phase V1.2 FIX COMPLETE"
Write-Host "============================================================"

