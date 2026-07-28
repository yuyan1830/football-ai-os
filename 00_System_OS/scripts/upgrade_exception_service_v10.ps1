Write-Host "====================================="
Write-Host "Football AI OS"
Write-Host "Exception Service V1.0 Upgrade"
Write-Host "====================================="


$CORE_PATH="E:\football_v\00_System_OS\01_DATA_LAYER\core"

$EXCEPTION_PATH="$CORE_PATH\exception"

$BACKUP_PATH="E:\football_v\99_DOCUMENTATION\checkpoints\exception_backup_v10"

$CHECKPOINT="E:\football_v\99_DOCUMENTATION\checkpoints\Checkpoint-027_Exception_Service_V1.0_Stable.txt"



# =========================
# Create backup folder
# =========================


New-Item `
-ItemType Directory `
-Path $BACKUP_PATH `
-Force | Out-Null



if(Test-Path $EXCEPTION_PATH){

Copy-Item `
$EXCEPTION_PATH `
$BACKUP_PATH `
-Recurse `
-Force

}



Write-Host ""
Write-Host "Exception backup completed"



# =========================
# Create exception folder
# =========================


New-Item `
-ItemType Directory `
-Path $EXCEPTION_PATH `
-Force | Out-Null



# =========================
# Base Exception
# =========================


@'

class FootballAIException(Exception):


    def __init__(

        self,

        message,

        code="SYSTEM_ERROR"

    ):


        self.message = message

        self.code = code


        super().__init__(message)



    def to_dict(self):


        return {


            "error":

            self.code,


            "message":

            self.message


        }

'@ | Out-File `
"$EXCEPTION_PATH\base_exception.py" `
-Encoding UTF8



# =========================
# Database Exception
# =========================


@'

from .base_exception import FootballAIException



class DatabaseException(FootballAIException):


    def __init__(self,message):


        super().__init__(

            message,

            "DATABASE_ERROR"

        )

'@ | Out-File `
"$EXCEPTION_PATH\database_exception.py" `
-Encoding UTF8



# =========================
# Validation Exception
# =========================


@'

from .base_exception import FootballAIException



class ValidationException(FootballAIException):


    def __init__(self,message):


        super().__init__(

            message,

            "VALIDATION_ERROR"

        )

'@ | Out-File `
"$EXCEPTION_PATH\validation_exception.py" `
-Encoding UTF8



# =========================
# File Exception
# =========================


@'

from .base_exception import FootballAIException



class FileServiceException(FootballAIException):


    def __init__(self,message):


        super().__init__(

            message,

            "FILE_ERROR"

        )

'@ | Out-File `
"$EXCEPTION_PATH\file_exception.py" `
-Encoding UTF8



# =========================
# Init
# =========================


@'

from .base_exception import FootballAIException
from .database_exception import DatabaseException
from .validation_exception import ValidationException
from .file_exception import FileServiceException


__all__=[

    "FootballAIException",

    "DatabaseException",

    "ValidationException",

    "FileServiceException"

]

'@ | Out-File `
"$EXCEPTION_PATH\__init__.py" `
-Encoding UTF8



Write-Host ""
Write-Host "Exception Service created"



# =========================
# Checkpoint
# =========================


@'

Football AI OS

Checkpoint-027

Module:

Exception Service


Version:

V1.0


Created:

core/exception


Components:

base_exception.py

database_exception.py

validation_exception.py

file_exception.py


Integration:

Logger compatible

Core Service compatible


Status:

Stable


'@ | Out-File `
$CHECKPOINT `
-Encoding UTF8



Write-Host ""
Write-Host "Checkpoint Created:"
Write-Host $CHECKPOINT



# =========================
# Test
# =========================


Write-Host ""
Write-Host "Testing Exception Service..."


cd E:\football_v\00_System_OS\01_DATA_LAYER


python -c "from core.exception import FootballAIException,DatabaseException,ValidationException,FileServiceException; print(FootballAIException('test').to_dict()); print(DatabaseException('db error').to_dict())"



Write-Host ""
Write-Host "Exception Service V1.0 Completed"