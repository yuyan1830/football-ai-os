# ============================================================
# Football AI OS Application Layer V2.5 REAL ALL FIX
# ============================================================


$base="E:\football_v"


$py="$base\deployment_scripts\application_layer_V2.5_initializer.py"


$report="$base\99_Documentation\reports\FOOTBALL_AI_OS_APPLICATION_LAYER_V2.5_REAL_REPORT.json"



Write-Host ""
Write-Host "============================================================"
Write-Host "Football AI OS APPLICATION LAYER V2.5 REAL ALL FIX"
Write-Host "============================================================"



# ============================================================
# 1. INITIALIZE APPLICATION LAYER
# ============================================================


Write-Host ""
Write-Host "[1] INITIALIZE APPLICATION LAYER"
Write-Host "=============================="


python $py



# ============================================================
# 2. DATABASE TEST
# ============================================================


Write-Host ""
Write-Host "[2] DATABASE TEST"
Write-Host "=============================="


$db="$base\09_APPLICATION_LAYER\runtime\application_runtime.db"


$tmp="$base\deployment_scripts\application_layer_db_test_tmp.py"



@"

import sqlite3


db=r'$db'


conn=sqlite3.connect(db)


print("TABLES")


for x in conn.execute(

"select name from sqlite_master where type='table'"

):

    print(x[0])



print("")


print("REGISTRY COUNT")


print(

conn.execute(

"select count(*) from application_registry"

).fetchone()[0]

)



conn.close()

"@ | Set-Content `
$tmp `
-Encoding UTF8



python $tmp



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
Write-Host "[4] APPLICATION TREE"
Write-Host "=============================="


tree "$base\09_APPLICATION_LAYER" /F



Write-Host ""

Write-Host "============================================================"

Write-Host "Football AI OS APPLICATION LAYER V2.5 REAL COMPLETE"

Write-Host "STATUS : READY"

Write-Host "============================================================"


