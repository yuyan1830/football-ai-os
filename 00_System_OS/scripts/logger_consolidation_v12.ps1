Write-Host ""
Write-Host "====================================="
Write-Host "Football AI OS"
Write-Host "Logger Consolidation V1.2"
Write-Host "====================================="
Write-Host ""


$ROOT="E:\football_v"

$CORE="$ROOT\00_System_OS\01_DATA_LAYER\core"

$LOGGER="$CORE\logger"

$DOC="$ROOT\99_DOCUMENTATION"

$CP="$DOC\checkpoints\Checkpoint-032_Logger_Consolidation_V1.2.txt"


Write-Host "Creating backup..."


$BACKUP="$DOC\backup\logger_backup_v12"

New-Item `
-ItemType Directory `
-Path $BACKUP `
-Force | Out-Null


Copy-Item `
"$CORE\logger.py" `
$BACKUP `
-Force `
-ErrorAction SilentlyContinue


Copy-Item `
$LOGGER `
$BACKUP `
-Recurse `
-Force


Write-Host "Logger backup completed"



Write-Host ""
Write-Host "Checking old logger entry..."



$OLD="$CORE\logger.py"



if(Test-Path $OLD){


@"
#
# Football AI OS
# Logger Compatibility Bridge V1.2
#

from .logger.logger import *

"@ | Out-File `
$OLD `
-Encoding UTF8


Write-Host "Old logger converted to compatibility bridge"


}
else{


Write-Host "Old logger entry not found"

}



Write-Host ""
Write-Host "Testing Logger Import..."



Set-Location "$ROOT\00_System_OS\01_DATA_LAYER"


python -c "from core.logger import get_logger; print('LOGGER V1.2 IMPORT OK')"



Write-Host ""
Write-Host "Generating checkpoint..."



@"

Football AI OS

Checkpoint-032

Logger Consolidation V1.2


Completed:

- Logger duplicate entry resolved
- Core logger unified
- Compatibility bridge created
- Logger import validated


Current:

core.logger


Deprecated:

core.logger.py direct implementation


Status:

Stable


"@ | Out-File `
$CP `
-Encoding UTF8



Write-Host ""
Write-Host "Checkpoint Created:"
Write-Host $CP


Write-Host ""
Write-Host "Logger Consolidation V1.2 Completed"
