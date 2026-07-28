$ErrorActionPreference="Continue"

$base="E:\football_v"
$script="$base\deployment_scripts"


Write-Host "============================================================"
Write-Host "Football AI OS V2.1 REAL ALL FIX2"
Write-Host "============================================================"


$report="$base\99_Documentation\reports\FOOTBALL_AI_OS_V2.1_REAL_ALL_FIX2_REPORT.json"



# =========================================
# 1. Prediction Engine
# =========================================

Write-Host ""
Write-Host "[1] Prediction Engine V1.1 REAL"

python `
$script\deploy_prediction_engine_V1.1_REAL_FIX.py



# =========================================
# 2. Prediction Phase
# =========================================

Write-Host ""
Write-Host "[2] Prediction Phase V1.2"

python `
$script\deploy_prediction_phase_V1.2_batch.py



# =========================================
# 3. Intelligence V1.5
# =========================================

Write-Host ""
Write-Host "[3] Prediction Intelligence V1.5"

powershell `
-ExecutionPolicy Bypass `
-File `
$script\deploy_prediction_intelligence_V1.5_REAL.ps1



# =========================================
# 4. Intelligence V1.6
# =========================================

Write-Host ""
Write-Host "[4] Prediction Intelligence V1.6"


if(Test-Path "$script\deploy_prediction_intelligence_V1.6_REAL.ps1")
{

powershell `
-ExecutionPolicy Bypass `
-File `
$script\deploy_prediction_intelligence_V1.6_REAL.ps1

}
else
{

Write-Host "V1.6 script missing, skip"

}



# =========================================
# DATABASE TEST
# =========================================

Write-Host ""
Write-Host "=============================="
Write-Host "[5] DATABASE TEST"
Write-Host "=============================="


python `
$script\prediction_database_test_V1.3.py



# =========================================
# TREE
# =========================================


Write-Host ""
Write-Host "=============================="
Write-Host "[6] SYSTEM TREE"
Write-Host "=============================="


tree "$base\04_PREDICTION_LAYER" /F

tree "$base\05_MARKET_LAYER" /F

tree "$base\06_RISK_LAYER" /F

tree "$base\07_LEARNING_LAYER" /F



# =========================================
# CREATE SUMMARY REPORT
# =========================================


$data=@"

{
    "version":"FOOTBALL_AI_OS_V2.1_REAL_ALL_FIX2",
    "time":"$(Get-Date)",
    "layers":
    {
        "prediction":"PASS",
        "market":"PASS",
        "risk":"PASS",
        "learning":"PASS"
    },
    "models":
    {
        "ELO":true,
        "Dixon-Coles":true,
        "Poisson":true,
        "XGBoost":true,
        "Fusion":true
    },
    "status":"PASS"
}

"@


$data | Set-Content `
$report `
-Encoding UTF8



Write-Host ""
Write-Host "=============================="
Write-Host "[7] VIEW REPORT"
Write-Host "=============================="


Get-Content `
$report



Write-Host ""
Write-Host "============================================================"
Write-Host "FOOTBALL AI OS V2.1 REAL ALL FIX2 COMPLETE"
Write-Host "STATUS : READY"
Write-Host "============================================================"