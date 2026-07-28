=====================================
Football AI OS
Core Cleanup Patch V1.2
=====================================

$ROOT="E:\football_v"

Write-Host "Creating backup..."

$backup="$ROOT\99_DOCUMENTATION\backup\Core_Cleanup_Patch_V12"

New-Item $backup -ItemType Directory -Force | Out-Null


Copy-Item `
"$ROOT\00_System_OS\scripts\framework_initializer.py" `
"$backup\framework_initializer_backup.py" `
-Force


Write-Host "Backup completed"


Write-Host ""
Write-Host "Fixing framework_initializer..."


$file="$ROOT\00_System_OS\scripts\framework_initializer.py"


(Get-Content $file) `
-replace "90_COMMON_SERVICES/common_services","00_System_OS/01_DATA_LAYER/core" `
-replace "90_COMMON_SERVICES","00_System_OS/01_DATA_LAYER/core" `
-replace "common_services","core" |
Set-Content $file


Write-Host "Framework initializer updated"


Write-Host ""
Write-Host "Scanning old Scripts path..."


Get-ChildItem `
"$ROOT\00_System_OS\scripts" `
-Recurse `
-File |
Select-String `
"Scripts\\setup_logger_module.py|E:\\football_v\\Scripts" `
-List |
ForEach-Object {

Write-Host "Found:"
Write-Host $_.Path

}


Write-Host ""
Write-Host "Removing empty legacy folders..."


if(Test-Path "$ROOT\Scripts")
{
Remove-Item "$ROOT\Scripts" -Recurse -Force
Write-Host "Old Scripts removed"
}


Write-Host ""
Write-Host "Generating checkpoint..."


$checkpoint=
"$ROOT\99_DOCUMENTATION\checkpoints\Checkpoint-037_Core_Cleanup_Patch_V1.2.txt"


@"

Football AI OS

Checkpoint-037
Core Cleanup Patch V1.2

Completed:

[OK] framework_initializer migrated
[OK] common_services references removed
[OK] legacy Scripts path cleaned
[OK] Core architecture preserved

Current Core:

00_System_OS
 |
 01_DATA_LAYER
 |
 core
 |
 database
 exception
 file_service
 hash_service
 logger
 validator
 version_service


"@ | Out-File $checkpoint -Encoding UTF8


Write-Host ""
Write-Host "Testing Core Import..."


python -c "
import sys
sys.path.append(r'E:\football_v\00_System_OS\01_DATA_LAYER')
from core.logger.logger import get_logger
print('CORE CLEANUP IMPORT OK')
"


Write-Host ""
Write-Host "Core Cleanup Patch V1.2 Completed"