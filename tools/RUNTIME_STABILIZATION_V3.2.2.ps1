# ==========================================================
# Football AI OS Ω+ V3.2.2
# Runtime Stabilization
# Clean Version
# ==========================================================


$ProjectRoot="E:\football_v"

$ValidationRoot="$ProjectRoot\99_DOCUMENTATION\validation"

$BackupRoot="$ProjectRoot\99_DOCUMENTATION\backup_runtime_fix_V3.2.2"



Write-Host ""
Write-Host "========================================"
Write-Host " Football AI OS Ω+ V3.2.2"
Write-Host " Runtime Stabilization"
Write-Host "========================================"
Write-Host ""



# ==========================================================
# 1 Environment Check
# ==========================================================


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



# ==========================================================
# 2 Backup
# ==========================================================


Write-Host ""
Write-Host "[2] Backup Existing Files"



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

    $destination="$BackupRoot\$file"


    if(Test-Path $source){


        $dir=Split-Path $destination


        New-Item `
        -ItemType Directory `
        -Path $dir `
        -Force | Out-Null



        Copy-Item `
        -Path $source `
        -Destination $destination `
        -Force



        Write-Host "[BACKUP] $file"


    }


}




# ==========================================================
# 3 Python Check
# ==========================================================


Write-Host ""
Write-Host "[3] Python Environment"



python --version



$imports=@(
"numpy",
"pandas",
"sklearn",
"xgboost",
"sqlalchemy"
)



foreach($m in $imports){


python -c "import $m;print('$m OK')" 


}




# ==========================================================
# 4 Model Layer Check
# ==========================================================


Write-Host ""
Write-Host "[4] MODEL_LAYER Check"



$modelRoot="$ProjectRoot\05_MODEL_AI\MODEL_LAYER"


$pyFiles=Get-ChildItem `
$modelRoot `
-Recurse `
-Filter *.py



Write-Host "Python Files:"
Write-Host $pyFiles.Count



$modelFiles=@(

"models\elo_model.py",

"models\dixon_coles_model.py",

"models\poisson_model.py",

"models\xgboost_model.py",

"fusion\fusion_engine.py",

"fusion\probability_calculator.py"

)



foreach($f in $modelFiles){


if(Test-Path "$modelRoot\$f"){

Write-Host "[PASS] $f"

}
else{

Write-Host "[FAIL] $f"

}


}




# ==========================================================
# 5 Feature Store Check
# ==========================================================


Write-Host ""
Write-Host "[5] Feature Store"



$db="$ProjectRoot\02_FEATURE_LAYER\database\feature_store.db"



if(Test-Path $db){


    Write-Host "[PASS] feature_store.db"


    $size=(Get-Item $db).Length


    Write-Host "Database Size:" $size "bytes"


}
else{


    Write-Host "[FAIL] feature_store.db"


}





# ==========================================================
# 6 Prediction Engine Check
# ==========================================================


Write-Host ""
Write-Host "[6] Prediction Engine"



$prediction="$ProjectRoot\06_PREDICTION_INTELLIGENCE_ENGINE"



if(Test-Path $prediction){


Get-ChildItem `
$prediction `
-Recurse `
-Filter *.py |
Measure-Object |
ForEach-Object{

Write-Host "Python Files:" $_.Count

}


}




# ==========================================================
# 7 Generate Report
# ==========================================================


Write-Host ""
Write-Host "[7] Generate Validation Report"



New-Item `
-ItemType Directory `
-Path $ValidationRoot `
-Force | Out-Null



$report=@"

Football AI OS Ω+ V3.2.2

Runtime Stabilization Report

Time:
$(Get-Date)


Status:

Environment Checked

Backup Completed

Model Layer Checked

Feature Store Checked

Prediction Engine Checked


"@



Set-Content `
"$ValidationRoot\V3.2.2_RUNTIME_STABILIZATION_REPORT.txt" `
$report `
-Encoding UTF8



Write-Host ""
Write-Host "========================================"
Write-Host " Runtime Stabilization Completed"
Write-Host "========================================"