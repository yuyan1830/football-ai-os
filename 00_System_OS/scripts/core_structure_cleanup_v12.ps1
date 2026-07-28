Write-Host ""
Write-Host "====================================="
Write-Host "Football AI OS"
Write-Host "Core Structure Cleanup V1.2"
Write-Host "====================================="
Write-Host ""


$ROOT="E:\football_v"

$CORE="$ROOT\00_System_OS\01_DATA_LAYER\core"

$SCRIPT="$ROOT\00_System_OS\scripts"

$DOC="$ROOT\99_DOCUMENTATION"

$CHECKPOINT="$DOC\checkpoints\Checkpoint-030_Core_Structure_V1.2.txt"

$BACKUP="$DOC\backup\Core_Backup_V1.2"


Write-Host "Creating backup..."


New-Item `
-ItemType Directory `
-Path $BACKUP `
-Force | Out-Null


Copy-Item `
-Path $CORE `
-Destination $BACKUP `
-Recurse `
-Force


Write-Host "Backup completed"


Write-Host ""
Write-Host "Creating new Core structure..."


$folders=@(

"$CORE\database",

"$CORE\file_service",

"$CORE\hash_service",

"$CORE\version_service"

)


foreach($f in $folders){

New-Item `
-ItemType Directory `
-Path $f `
-Force | Out-Null

}



Write-Host "Directory structure ready"



Write-Host ""
Write-Host "Moving services..."



Move-Item `
"$CORE\db_connection.py" `
"$CORE\database\db_connection.py" `
-Force



Move-Item `
"$CORE\file_service.py" `
"$CORE\file_service\file_service.py" `
-Force



Move-Item `
"$CORE\hash_service.py" `
"$CORE\hash_service\hash_service.py" `
-Force



Move-Item `
"$CORE\version_service.py" `
"$CORE\version_service\version_service.py" `
-Force



Write-Host "Core services moved"



Write-Host ""
Write-Host "Moving deployment scripts..."



$validatorScripts=@(

"deploy_schema_validator_final.ps1",

"upgrade_database_service_v11.ps1",

"upgrade_exception_service_v1.ps1",

"upgrade_validator_schema_v1.ps1"

)



foreach($file in $validatorScripts){


$source="$CORE\validator\$file"


if(Test-Path $source){


Move-Item `
$source `
$SCRIPT `
-Force


}



}



Write-Host "Scripts moved"



Write-Host ""
Write-Host "Cleaning pycache..."



Get-ChildItem `
$ROOT `
-Recurse `
-Directory `
-Filter "__pycache__" |
Remove-Item `
-Recurse `
-Force



Write-Host "Pycache cleaned"



Write-Host ""
Write-Host "Generating checkpoint..."



@"

Football AI OS

Checkpoint-030

Core Structure V1.2

Completed:

- Core service layer cleanup
- Database service separation
- File service separation
- Hash service separation
- Version service separation
- Deployment scripts relocation

Legacy:

90_COMMON_SERVICES Removed

Current:

00_System_OS
 ©¸©¤©¤01_DATA_LAYER
      ©¸©¤©¤core


Status:

Stable

"@ | Out-File `
$CHECKPOINT `
-Encoding UTF8



Write-Host ""
Write-Host "Checkpoint Created:"
Write-Host $CHECKPOINT



Write-Host ""
Write-Host "Testing Core Import..."



Set-Location "$ROOT\00_System_OS\01_DATA_LAYER"


python -c "from core.database.db_connection import get_connection; print('CORE V1.2 IMPORT OK')"



Write-Host ""

Write-Host "Core Structure Cleanup V1.2 Completed"

Write-Host ""