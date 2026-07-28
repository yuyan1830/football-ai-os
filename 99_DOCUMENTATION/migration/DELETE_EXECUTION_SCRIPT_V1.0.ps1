$ROOT="E:\football_v"

$DOC="$ROOT\99_DOCUMENTATION\migration"

$LIST="$DOC\FINAL_MIGRATION_DELETE_READY_LIST_V1.0.csv"


$TIME=Get-Date -Format "yyyyMMdd_HHmmss"


$BACKUP="$ROOT\99_DOCUMENTATION\migration\backup_$TIME"


$LOG="$DOC\DELETE_EXECUTION_LOG_$TIME.txt"



New-Item -ItemType Directory -Force -Path $BACKUP | Out-Null



if (!(Test-Path $LIST)) {

    Write-Host "找不到删除清单"

    exit

}



"Football AI OS DELETE EXECUTION LOG" | Out-File $LOG

"TIME: $(Get-Date)" | Out-File $LOG -Append

"" | Out-File $LOG -Append



$rows=Import-Csv $LIST



foreach($row in $rows){


    if($row.status -eq "SAFE_DELETE"){


        $file=$row.file



        $source=Join-Path $ROOT $file



        if(Test-Path $source){



            $target=Join-Path $BACKUP $file



            $targetDir=Split-Path $target



            New-Item -ItemType Directory -Force -Path $targetDir | Out-Null



            Move-Item $source $target -Force



            "MOVED : $file" | Out-File $LOG -Append


        }

        else{


            "NOT FOUND : $file" | Out-File $LOG -Append


        }


    }

    else{


        "SKIP REVIEW : $($row.file)" | Out-File $LOG -Append


    }

}



"" | Out-File $LOG -Append

"BACKUP LOCATION:" | Out-File $LOG -Append

$BACKUP | Out-File $LOG -Append



Write-Host "完成"

Write-Host "备份目录:"
Write-Host $BACKUP

Write-Host "日志:"
Write-Host $LOG

