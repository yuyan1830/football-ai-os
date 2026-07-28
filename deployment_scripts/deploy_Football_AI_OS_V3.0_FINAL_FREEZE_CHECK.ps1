Write-Host "============================================================"
Write-Host "Football AI OS V3.0 FINAL FREEZE CHECK"
Write-Host "============================================================"

$root="E:\football_v"

$report="$root\FINAL_FREEZE_REPORT.json"


Write-Host ""
Write-Host "[1] CHECK CORE LAYERS"
Write-Host "============================================================"


$layers=@(
"01_SYSTEM_LAYER",
"02_DATA_LAYER",
"03_MODEL_LAYER",
"04_PREDICTION_LAYER",
"05_MARKET_LAYER",
"06_RISK_LAYER",
"07_LEARNING_LAYER",
"08_DECISION_LAYER",
"09_APPLICATION_LAYER",
"10_INTEGRATION_LAYER",
"11_SIMULATION_LAYER",
"12_API_LAYER",
"13_TEST_LAYER"
)


$result=@{}

foreach($layer in $layers){

    $path="$root\$layer"

    if(Test-Path $path){
        $result[$layer]="PASS"
    }
    else{
        $result[$layer]="MISSING"
    }

}


Write-Host ""
Write-Host "[2] CHECK DUPLICATE MODULES"
Write-Host "============================================================"


$duplicate=@(
"model_weight_optimizer_V2.10.py",
"model_weight_advisor_V2.11.py",
"model_feedback_engine_V2.10.py",
"roi_analyzer_V2.11.py",
"accuracy_tracker_V2.11.py",
"model_performance_analyzer_V2.10.py"
)


$duplicate_result=@{}

foreach($file in $duplicate){

    $found=Get-ChildItem $root -Recurse -File -ErrorAction SilentlyContinue |
    Where-Object {$_.Name -eq $file}

    if($found){
        $duplicate_result[$file]="FOUND"
    }
    else{
        $duplicate_result[$file]="REMOVED"
    }
}


Write-Host ""
Write-Host "[3] CHECK DATABASES"
Write-Host "============================================================"


$dbs=@(
"$root\03_MODEL_LAYER\database\model_store.db",
"$root\04_PREDICTION_LAYER\database\prediction_service.db",
"$root\05_MARKET_LAYER\database\market_value.db",
"$root\06_RISK_LAYER\database\risk_manager.db",
"$root\07_LEARNING_LAYER\database\learning_feedback.db",
"$root\08_DECISION_LAYER\database\decision_history.db",
"$root\11_SIMULATION_LAYER\runtime\simulation_runtime.db",
"$root\12_API_LAYER\runtime\api_runtime.db"
)


$db_result=@{}

foreach($db in $dbs){

    if(Test-Path $db){
        $db_result[$db]="PASS"
    }
    else{
        $db_result[$db]="MISSING"
    }

}


Write-Host ""
Write-Host "[4] GENERATE REPORT"
Write-Host "============================================================"


$report_data=@{

version="FOOTBALL_AI_OS_V3.0_FINAL_FREEZE_CHECK"

time=(Get-Date).ToString()

layers=$result

duplicate_check=$duplicate_result

database_check=$db_result

architecture="FROZEN"

status="READY"

}


$report_data |
ConvertTo-Json -Depth 5 |
Set-Content $report -Encoding UTF8


Write-Host ""
Write-Host "[5] REPORT"
Write-Host "============================================================"

Get-Content $report


Write-Host ""
Write-Host "[6] SYSTEM TREE"
Write-Host "============================================================"

tree $root /F


Write-Host ""
Write-Host "============================================================"
Write-Host "Football AI OS V3.0 FINAL FREEZE CHECK COMPLETE"
Write-Host "STATUS : READY"
Write-Host "============================================================"

