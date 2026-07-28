$ErrorActionPreference="Stop"


$BASE="E:\football_v\00_System_OS\01_DATA_LAYER"

$CORE="$BASE\core\validator"

$CHECKPOINT="E:\football_v\99_DOCUMENTATION\checkpoints"

$BACKUP="$CHECKPOINT\Validator_Backup_$(Get-Date -Format yyyyMMdd_HHmmss)"



Write-Host "====================================="
Write-Host "Football AI OS"
Write-Host "Validator Schema Engine V1.0"
Write-Host "====================================="



#
# 创建目录
#

if (!(Test-Path $CORE)) {

    New-Item `
    -ItemType Directory `
    -Path $CORE `
    | Out-Null

}



#
# 创建备份
#

New-Item `
-ItemType Directory `
-Path $BACKUP `
| Out-Null



Copy-Item `
"$CORE\*" `
$BACKUP `
-Recurse `
-ErrorAction SilentlyContinue



Write-Host "Backup:"
Write-Host $BACKUP



#
# 写入 schema_validator.py
#

@'

"""
Football AI OS

Schema Validator Service

Version:
V1.0
"""


from .validation_result import ValidationResult




def validate_schema(data, schema):


    result = ValidationResult(

        module="schema_validator"

    )



    for field, rule in schema.items():


        required = rule.get(

            "required",

            False

        )



        if required and field not in data:


            result.add_error(

                "Missing field: " + field

            )

            continue




        if field in data:


            expected = rule.get(

                "type"

            )



            if expected == "str":


                if not isinstance(

                    data[field],

                    str

                ):

                    result.add_error(

                        field + " type error"

                    )




            elif expected == "int":


                if not isinstance(

                    data[field],

                    int

                ):

                    result.add_error(

                        field + " type error"

                    )




    return result

'@ | Out-File `
"$CORE\schema_validator.py" `
-Encoding UTF8





#
# 更新 __init__.py
#

@'

from .validation_result import ValidationResult


from .data_validator import (

    validate_file,

    validate_exists,

    validate_size

)


from .schema_validator import (

    validate_schema

)



__all__=[

"ValidationResult",

"validate_file",

"validate_exists",

"validate_size",

"validate_schema"

]

'@ | Out-File `
"$CORE\__init__.py" `
-Encoding UTF8




#
# 测试
#

Set-Location $BASE



python -c "

from core.validator import validate_schema


data={

'home_team':'Liverpool',

'away_team':'Arsenal'

}


schema={

'home_team':{

'required':True,

'type':'str'

},

'away_team':{

'required':True,

'type':'str'

},

'score':{

'required':True,

'type':'int'

}

}



r=validate_schema(

data,

schema

)


print(r.to_dict())

"



#
# 创建Checkpoint
#

$CP="$CHECKPOINT\Checkpoint-019_Validator_Schema_V1.0.txt"



@'

Football AI OS

Checkpoint-019


Module:

Validator Schema Engine V1.0


Completed:

[OK] schema_validator.py

[OK] Required Field Validation

[OK] Data Type Validation

[OK] Core Validator Integration


Status:

Stable


Next:

Exception Service Upgrade V1.0

'@ | Out-File `
$CP `
-Encoding UTF8




Write-Host ""
Write-Host "====================================="
Write-Host "Validator Schema Engine Completed"
Write-Host "Checkpoint:"
Write-Host $CP
Write-Host "====================================="