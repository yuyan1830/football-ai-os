# ============================================================
# Football AI OS Model Layer V2.3 REAL ALL FIX2
# ============================================================

$base="E:\football_v"

$script="$base\deployment_scripts\model_layer_V2.3_initializer.py"

$report="$base\99_Documentation\reports\FOOTBALL_AI_OS_MODEL_LAYER_V2.3_REAL_REPORT.json"


Write-Host ""
Write-Host "============================================================"
Write-Host "Football AI OS MODEL LAYER V2.3 REAL ALL FIX2"
Write-Host "============================================================"


# ============================================================
# 1. RUN INITIALIZER
# ============================================================

Write-Host ""
Write-Host "[1] INITIALIZE MODEL LAYER"
Write-Host "=============================="


python $script



# ============================================================
# 2. DATABASE TEST
# ============================================================

Write-Host ""
Write-Host "[2] DATABASE TEST"
Write-Host "=============================="


python -c "
import sqlite3

db=r'E:\football_v\03_MODEL_LAYER\database\model_store_v23.db'

c=sqlite3.connect(db).cursor()

print('TABLES:')

for x in c.execute(
\"select name from sqlite_master where type='table'\"
):

    print(x[0])

"



# ============================================================
# 3. VIEW REPORT
# ============================================================

Write-Host ""
Write-Host "[3] VIEW REPORT"
Write-Host "=============================="


if(Test-Path $report){

    Get-Content $report

}
else{

    Write-Host "REPORT NOT FOUND"

}



# ============================================================
# 4. TREE
# ============================================================


Write-Host ""
Write-Host "[4] MODEL TREE"
Write-Host "=============================="


tree "$base\03_MODEL_LAYER" /F



Write-Host ""
Write-Host "============================================================"
Write-Host "Football AI OS MODEL LAYER V2.3 REAL COMPLETE"
Write-Host "STATUS : READY"
Write-Host "============================================================"


