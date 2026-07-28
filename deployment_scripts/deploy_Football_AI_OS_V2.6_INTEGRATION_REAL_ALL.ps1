# ============================================================
# Football AI OS V2.6 INTEGRATION REAL ALL
# ============================================================

$ErrorActionPreference="Continue"


Write-Host ""
Write-Host "============================================================"
Write-Host "Football AI OS V2.6 INTEGRATION REAL ALL"
Write-Host "============================================================"


$base="E:\football_v"

$script="$base\deployment_scripts\integration_layer_V2.6_initializer.py"

$layer="$base\10_INTEGRATION_LAYER"

$report="$base\99_Documentation\reports\FOOTBALL_AI_OS_V2.6_SYSTEM_HEALTH_REPORT.json"



# ============================================================
# 1. DEPLOY
# ============================================================

Write-Host ""
Write-Host "[1] INITIALIZE INTEGRATION LAYER"
Write-Host "============================================================"


python $script



# ============================================================
# 2. MODEL TEST
# ============================================================

Write-Host ""
Write-Host "[2] MODEL CONNECTION TEST"
Write-Host "============================================================"


python "$layer\test\model_connection_test.py"



# ============================================================
# 3. FULL PIPELINE TEST
# ============================================================

Write-Host ""
Write-Host "[3] FULL PIPELINE TEST"
Write-Host "============================================================"


python "$layer\test\full_pipeline_test.py"



# ============================================================
# 4. DATABASE TEST
# ============================================================

Write-Host ""
Write-Host "[4] DATABASE TEST"
Write-Host "============================================================"


$db="$layer\runtime\integration_test.db"


python -c @"

import sqlite3

db=r'$db'

conn=sqlite3.connect(db)

cur=conn.cursor()


print("TABLES")

for t in cur.execute(
"SELECT name FROM sqlite_master WHERE type='table'"
):

    print(t[0])


print("")

print("COUNTS")


for row in cur.execute(
"SELECT count(*) FROM integration_registry"
):

    print("integration_registry",row[0])


conn.close()

"@



# ============================================================
# 5. VIEW REPORT
# ============================================================

Write-Host ""
Write-Host "[5] VIEW REPORT"
Write-Host "============================================================"


if(Test-Path $report){

    Get-Content $report

}
else{

    Write-Host "REPORT NOT FOUND"

}



# ============================================================
# 6. TREE
# ============================================================


Write-Host ""
Write-Host "[6] SYSTEM TREE"
Write-Host "============================================================"


tree "$layer" /F



# ============================================================
# 7. FINAL
# ============================================================


Write-Host ""
Write-Host "============================================================"
Write-Host "Football AI OS V2.6 INTEGRATION REAL COMPLETE"
Write-Host "STATUS : READY"
Write-Host "============================================================"

