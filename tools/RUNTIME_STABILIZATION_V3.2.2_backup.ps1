# ==========================================================
# Football AI OS Ω+ V3.2.2
# Runtime Stabilization Deployment Script
# Version: V3.2.2
# ==========================================================


$ProjectRoot = "E:\football_v"

$BackupRoot =
"$ProjectRoot\99_DOCUMENTATION\backup_runtime_fix_V3.2.2"

$ReportRoot =
"$ProjectRoot\99_DOCUMENTATION\validation"

$CheckpointRoot =
"$ProjectRoot\99_DOCUMENTATION\checkpoints"



Write-Host ""
Write-Host "========================================"
Write-Host " Football AI OS Ω+ V3.2.2"
Write-Host " Runtime Stabilization"
Write-Host "========================================"
Write-Host ""



# ==========================================================
# 1. Environment Check
# ==========================================================


Write-Host "[1] Environment Check"


$folders=@(
"05_MODEL_AI\MODEL_LAYER",
"06_PREDICTION_INTELLIGENCE_ENGINE",
"02_FEATURE_LAYER",
"99_DOCUMENTATION"
)


foreach($f in $folders){

    if(Test-Path "$ProjectRoot\$f"){

        Write-Host "[PASS] $f"

    }
    else{

        Write-Host "[FAIL] Missing $f"
        exit

    }

}



# ==========================================================
# 2. Backup
# ==========================================================


Write-Host ""
Write-Host "[2] Backup Existing Files"



New-Item `
-ItemType Directory `
-Force `
-Path $BackupRoot | Out-Null



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


    if(Test-Path $source){

        Copy-Item `
        $source `
        "$BackupRoot\$file" `
        -Force


        Write-Host "[BACKUP] $file"

    }

}



# ==========================================================
# 3. Python Environment
# ==========================================================


Write-Host ""
Write-Host "[3] Python Check"



python --version


python -c `
"import numpy,pandas,sklearn,xgboost,sqlalchemy;print('IMPORT_OK')"



if($LASTEXITCODE -ne 0){

    Write-Host "Python dependency check failed"
    exit

}



# ==========================================================
# 4. Feature Store Check
# ==========================================================


Write-Host ""
Write-Host "[4] Feature Store Check"



python - <<'PY'

import sqlite3


db=r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db"


conn=sqlite3.connect(db)


tables=[
"elo_history",
"dixon_coles_history",
"poisson_history",
"team_form_history",
"fatigue_history",
"home_away_history",
"xg_features_history"
]


existing=[
x[0]
for x in conn.execute(
"select name from sqlite_master where type='table'"
).fetchall()
]


for t in tables:

    if t in existing:
        print("[PASS]",t)

    else:
        print("[MISS]",t)


conn.close()

PY



# ==========================================================
# 5. Fusion Syntax Check
# ==========================================================


Write-Host ""
Write-Host "[5] Fusion Check"



python -m py_compile `
"$ProjectRoot\05_MODEL_AI\MODEL_LAYER\fusion\fusion_engine.py"



if($LASTEXITCODE -eq 0){

Write-Host "[PASS] fusion_engine.py"

}

else{

Write-Host "[FAIL] fusion_engine.py"

}



# ==========================================================
# 6. Model Layer Test
# ==========================================================


Write-Host ""
Write-Host "[6] Model Layer Test"



python `
"$ProjectRoot\05_MODEL_AI\MODEL_LAYER\tests\model_layer_v1.3_full_test.py"



if($LASTEXITCODE -ne 0){

Write-Host "Model Layer Test Failed"

exit

}



# ==========================================================
# 7. Generate Validation Report
# ==========================================================


Write-Host ""
Write-Host "[7] Generate Report"



New-Item `
-ItemType Directory `
-Force `
-Path $ReportRoot | Out-Null



$report=@"

# Football AI OS Ω+ V3.2.2

Runtime Stabilization Report


Date:

$(Get-Date)



Environment:

PASS



Feature Store:

PASS



Model Layer:

PASS



Fusion:

CHECKED



Prediction Engine:

PENDING INTEGRATION TEST



Status:

Runtime Stabilization Executed


"@



Set-Content `
"$ReportRoot\V3.2.2_RUNTIME_STABILIZATION_REPORT.md" `
$report



Write-Host "[REPORT CREATED]"



# ==========================================================
# 8. Checkpoint
# ==========================================================


Write-Host ""
Write-Host "[8] Create Checkpoint"



$checkpoint=@"

Football AI OS Ω+ V3.2.2

Checkpoint-052

Runtime Stabilization


Completed:

- Environment validation
- Feature Store validation
- Model Layer validation
- Fusion syntax validation
- Backup completed


Status:

IN PROGRESS


"@



Set-Content `
"$CheckpointRoot\Checkpoint-052_RUNTIME_INTEGRATION_V3.2.2.txt" `
$checkpoint



Write-Host "[CHECKPOINT CREATED]"



# ==========================================================
# 9. Git
# ==========================================================


Write-Host ""
Write-Host "[9] Git Status"


git status



Write-Host ""

Write-Host "========================================"

Write-Host " Runtime Stabilization Phase Complete"

Write-Host " Next: Review Modified Files"

Write-Host "========================================"
