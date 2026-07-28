Write-Host ""
Write-Host "====================================="
Write-Host "Football AI OS"
Write-Host "Logger Cleanup V1.3"
Write-Host "====================================="
Write-Host ""


$ROOT="E:\football_v"

$CORE="$ROOT\00_System_OS\01_DATA_LAYER\core"

$OLD="$CORE\logger.py"

$LOGGER="$CORE\logger"

$BACKUP="$ROOT\99_DOCUMENTATION\backup\logger_cleanup_v13"

$CP="$ROOT\99_DOCUMENTATION\checkpoints\Checkpoint-034_Logger_Cleanup_V1.3.txt"


Write-Host "Creating backup..."


New-Item `
-ItemType Directory `
-Path $BACKUP `
-Force | Out-Null


if(Test-Path $OLD){

Copy-Item `
$OLD `
$BACKUP `
-Force

Write-Host "Old logger backup completed"

}
else{

Write-Host "Old logger.py not found"

}



Write-Host ""
Write-Host "Removing duplicate logger entry..."



if(Test-Path $OLD){

Remove-Item `
$OLD `
-Force

Write-Host "core\logger.py removed"

}
else{

Write-Host "Nothing to remove"

}



Write-Host ""
Write-Host "Testing Logger Import..."



Set-Location "$ROOT\00_System_OS\01_DATA_LAYER"


python -c "
from core.logger import get_logger
print('LOGGER SINGLE ENTRY OK')
"



Write-Host ""
Write-Host "Generating checkpoint..."



@"

Football AI OS

Checkpoint-034

Logger Cleanup V1.3


Completed:

Removed duplicate logger.py

Unified logger entry:

core.logger


Validation:

LOGGER SINGLE ENTRY OK


Current Architecture:

core
 |
 ©¸©¤©¤logger


Status:

Stable


"@ | Out-File `
$CP `
-Encoding UTF8



Write-Host ""
Write-Host "Checkpoint Created:"
Write-Host $CP


Write-Host ""
Write-Host "Logger Cleanup V1.3 Completed"
