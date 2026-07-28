# ============================================================
# Football AI OS Decision Layer V2.4 REAL ALL FIX
# ============================================================


$base="E:\football_v"


$py="$base\deployment_scripts\decision_layer_V2.4_initializer.py"


$report="$base\99_Documentation\reports\FOOTBALL_AI_OS_DECISION_LAYER_V2.4_REAL_REPORT.json"



Write-Host ""
Write-Host "============================================================"
Write-Host "Football AI OS DECISION LAYER V2.4 REAL ALL FIX"
Write-Host "============================================================"



# ============================================================
# 1. INITIALIZE
# ============================================================


Write-Host ""
Write-Host "[1] INITIALIZE DECISION LAYER"
Write-Host "=============================="


python $py



# ============================================================
# 2. DATABASE TEST
# ============================================================


Write-Host ""
Write-Host "[2] DATABASE TEST"
Write-Host "=============================="


$db="$base\08_DECISION_LAYER\database\decision_history.db"


$test="$base\deployment_scripts\decision_layer_db_test_tmp.py"



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


print("COUNTS")


for t in [

"decision_history",

"decision_registry"

]:


    try:

        c=conn.execute(

        f"select count(*) from {t}"

        ).fetchone()[0]


        print(t,c)


    except Exception as e:

        print(t,"ERROR")


conn.close()

"@ | Set-Content `
$test `
-Encoding UTF8



python $test




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
Write-Host "[4] DECISION LAYER TREE"
Write-Host "=============================="


tree "$base\08_DECISION_LAYER" /F



Write-Host ""

Write-Host "============================================================"

Write-Host "Football AI OS DECISION LAYER V2.4 REAL COMPLETE"

Write-Host "STATUS : READY"

Write-Host "============================================================"


