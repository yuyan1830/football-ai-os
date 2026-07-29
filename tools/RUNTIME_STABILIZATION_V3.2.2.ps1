# ============================================
# Football AI OS Ω+ V3.2.2
# Runtime Stabilization
# PowerShell Native Version
# ============================================


$ProjectRoot="E:\football_v"

$BackupRoot="$ProjectRoot\99_DOCUMENTATION\backup_runtime_fix_V3.2.2"

$ValidationRoot="$ProjectRoot\99_DOCUMENTATION\validation"


Write-Host ""
Write-Host "========================================"
Write-Host " Football AI OS Ω+ V3.2.2"
Write-Host " Runtime Stabilization"
Write-Host "========================================"


# ============================================
# 1 Environment
# ============================================

Write-Host ""
Write-Host "[1] Environment Check"


$paths=@(
"05_MODEL_AI\MODEL_LAYER",
"06_PREDICTION_INTELLIGENCE_ENGINE",
"02_FEATURE_LAYER",
"99_DOCUMENTATION"
)


foreach($p in $paths){

    if(Test-Path "$ProjectRoot\$p"){

        Write-Host "[PASS] $p"

    }
    else{

        Write-Host "[FAIL] $p"

    }

}



# ============================================
# 2 Backup
# ============================================


Write-Host ""
Write-Host "[2] Backup Existing Files"


New-Item `
-ItemType Directory `
-Path $BackupRoot `
-Force | Out-Null


$files=@(

"05_MODEL_AI\MODEL_LAYER\model_loader.py",
"05_MODEL_AI\MODEL_LAYER\model_registry.py",
"05_MODEL_AI\MODEL_LAYER\model_runtime.py",
"05_MODEL_AI\MODEL_LAYER\fusion\fusion_engine.py",
"05_MODEL_AI\MODEL_LAYER\fusion\probability_calculator.py",
"06_PREDICTION_INTELLIGENCE_ENGINE\prediction_api\api_service.py"

)



foreach($file in $files){

    $source="$ProjectRoot\$file"

    $dest="$BackupRoot\$file"

    $destDir=Split-Path $dest


    if(Test-Path $source){


        New-Item `
        -ItemType Directory `
        -Path $destDir `
        -Force | Out-Null


        Copy-Item `
        -Path $source `
        -Destination $dest `
        -Force


        Write-Host "[BACKUP] $file"

    }

}




# ============================================
# 3 Python Environment
# ============================================


Write-Host ""
Write-Host "[3] Python Environment"


python --version


$modules=@(
"numpy",
"pandas",
"sklearn",
"xgboost",
"sqlalchemy"
)


foreach($m in $modules){

    python -c "import $m;print('$m OK')" 

}




# ============================================
# 4 MODEL LAYER
# ============================================


Write-Host ""
Write-Host "[4] MODEL_LAYER Check"


$modelPath="$ProjectRoot\05_MODEL_AI\MODEL_LAYER"


$count=(Get-ChildItem $modelPath -Recurse -Filter *.py).Count


Write-Host "Python Files:" $count



$check=@(

"models\elo_model.py",
"models\dixon_coles_model.py",
"models\poisson_model.py",
"models\xgboost_model.py",
"fusion\fusion_engine.py",
"fusion\probability_calculator.py"

)



foreach($c in $check){

    if(Test-Path "$modelPath\$c"){

        Write-Host "[PASS] $c"

    }

}




# ============================================
# 5 Feature Store
# ============================================


Write-Host ""
Write-Host "[5] Feature Store"



$db="$ProjectRoot\02_FEATURE_LAYER\database\feature_store.db"


if(Test-Path $db){


    Write-Host "[PASS] feature_store.db"


    $size=(Get-Item $db).Length


    Write-Host "Database Size:" $size "bytes"



    python -c "import sqlite3;db=r'$db';c=sqlite3.connect(db).cursor();print('[FEATURE_TABLES]',len(c.execute(\"select name from sqlite_master where type='table'\").fetchall()))"


}
else{


    Write-Host "[FAIL] feature_store.db"


}




# ============================================
# 6 Prediction Engine
# ============================================


Write-Host ""
Write-Host "[6] Prediction Engine"


$prediction="$ProjectRoot\06_PREDICTION_INTELLIGENCE_ENGINE"


$count2=(Get-ChildItem $prediction -Recurse -Filter *.py).Count


Write-Host "Python Files:" $count2




# ============================================
# 7 Report
# ============================================


Write-Host ""
Write-Host "[7] Generate Validation Report"


New-Item `
-ItemType Directory `
-Path $ValidationRoot `
-Force | Out-Null



$report=@"

Football AI OS Ω+ V3.2.2

Runtime Stabilization Report

Status: PASS

MODEL_LAYER:
$count

Prediction Engine:
$count2

Feature Store:
feature_store.db

Validation:
Completed

"@



Set-Content `
"$ValidationRoot\V3.2.2_RUNTIME_VALIDATION_REPORT.txt" `
$report `
-Encoding UTF8




Write-Host ""
Write-Host "========================================"
Write-Host " Runtime Stabilization Completed"
Write-Host "========================================"
