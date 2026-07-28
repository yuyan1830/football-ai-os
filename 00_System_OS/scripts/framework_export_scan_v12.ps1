# =====================================
# Football AI OS
# Framework Export Scanner V1.2
# =====================================


$ROOT="E:\football_v"

$OUT="$ROOT\99_DOCUMENTATION\reports\Framework_Export_Scan_V1.2"


New-Item `
$OUT `
-ItemType Directory `
-Force | Out-Null



Write-Host ""
Write-Host "====================================="
Write-Host "Football AI OS Framework Export V1.2"
Write-Host "====================================="



# 1. Full tree

Write-Host ""
Write-Host "Exporting directory tree..."


tree $ROOT /F /A `
> "$OUT\full_tree.txt"



# 2. Python modules


Write-Host "Scanning Python modules..."


Get-ChildItem `
$ROOT `
-Recurse `
-Filter *.py |
Select-Object FullName |
Out-File `
"$OUT\python_modules.txt" `
-Encoding UTF8




# 3. PowerShell scripts


Write-Host "Scanning PowerShell scripts..."


Get-ChildItem `
$ROOT `
-Recurse `
-Filter *.ps1 |
Select-Object FullName |
Out-File `
"$OUT\powershell_scripts.txt" `
-Encoding UTF8




# 4. Core structure


Write-Host "Exporting Core structure..."


tree `
"$ROOT\00_System_OS\01_DATA_LAYER\core" `
/F /A |
Out-File `
"$OUT\core_structure.txt" `
-Encoding UTF8




# 5. Data Layer


Write-Host "Exporting Data Layer..."


tree `
"$ROOT\00_System_OS\01_DATA_LAYER" `
/F /A |
Out-File `
"$OUT\data_layer_structure.txt" `
-Encoding UTF8




# 6. Documentation


Write-Host "Exporting checkpoints..."


Get-ChildItem `
"$ROOT\99_DOCUMENTATION\checkpoints" |
Select Name |
Out-File `
"$OUT\checkpoints_list.txt" `
-Encoding UTF8




# 7. File statistics


Write-Host "Generating statistics..."


$total=(Get-ChildItem `
$ROOT `
-Recurse `
-File).Count


$py=(Get-ChildItem `
$ROOT `
-Recurse `
-Filter *.py).Count


$ps=(Get-ChildItem `
$ROOT `
-Recurse `
-Filter *.ps1).Count



@"

Football AI OS Framework Export Report

Version:
V1.2


Root:

$ROOT


Statistics:

Total Files:
$total


Python Files:
$py


PowerShell Files:
$ps



Core:

00_System_OS
 |
 01_DATA_LAYER
 |
 core



Generated:
$(Get-Date)


"@ |

Out-File `
"$OUT\framework_report.txt" `
-Encoding UTF8




Write-Host ""
Write-Host "====================================="
Write-Host "Framework Export Completed"
Write-Host ""
Write-Host "Output:"
Write-Host $OUT
Write-Host "====================================="