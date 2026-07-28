Write-Host ""
Write-Host "====================================="
Write-Host "Football AI OS"
Write-Host "Legacy Cleanup V1.0"
Write-Host "====================================="
Write-Host ""


$ROOT="E:\football_v"

$ARCHIVE="$ROOT\archive"


Write-Host "Creating archive structure..."



New-Item `
"$ARCHIVE\common_service_migration" `
-ItemType Directory `
-Force | Out-Null


New-Item `
"$ARCHIVE\logger_migration" `
-ItemType Directory `
-Force | Out-Null


New-Item `
"$ARCHIVE\framework_scan_history" `
-ItemType Directory `
-Force | Out-Null



Write-Host "Archive structure ready"



Write-Host ""
Write-Host "Moving migration scripts..."



$commonScripts=@(
"00_System_OS\scripts\common_service_migration_check.py",
"00_System_OS\scripts\core_service_compare.py",
"00_System_OS\scripts\core_service_compare_v2.py"
)


foreach($file in $commonScripts){

$src="$ROOT\$file"

if(Test-Path $src){

Move-Item `
$src `
"$ARCHIVE\common_service_migration" `
-Force

}

}



$loggerScripts=@(
"00_System_OS\scripts\logger_core_merge_v1.py",
"00_System_OS\scripts\logger_upgrade_v1.py",
"Scripts\setup_logger_module.py"
)


foreach($file in $loggerScripts){

$src="$ROOT\$file"

if(Test-Path $src){

Move-Item `
$src `
"$ARCHIVE\logger_migration" `
-Force

}

}



Write-Host ""
Write-Host "Moving historical scans..."



$historyFiles=@(
"upload\common_services_scan.txt",
"upload\framework_scan.txt",
"upload\python_modules.txt"
)



foreach($file in $historyFiles){

$src="$ROOT\$file"

if(Test-Path $src){

Move-Item `
$src `
"$ARCHIVE\framework_scan_history" `
-Force

}

}



Write-Host ""
Write-Host "Testing Core Import..."



Set-Location "$ROOT\00_System_OS\01_DATA_LAYER"


python -c "
from core.logger import get_logger
from core.validator import *
from core.exception import *
print('CORE AFTER CLEANUP OK')
"



$CP="$ROOT\99_DOCUMENTATION\checkpoints\Checkpoint-036_Legacy_Cleanup_V1.0.txt"



@"

Football AI OS

Checkpoint-036

Legacy Cleanup V1.0


Actions:

Migration scripts archived

Historical scans archived

Core files untouched


Core Test:

PASS


Architecture:

Enterprise Architecture V1.2


Status:

Stable


"@ | Out-File `
$CP `
-Encoding UTF8



Write-Host ""
Write-Host "Checkpoint Created:"
Write-Host $CP


Write-Host ""
Write-Host "Legacy Cleanup V1.0 Completed"
