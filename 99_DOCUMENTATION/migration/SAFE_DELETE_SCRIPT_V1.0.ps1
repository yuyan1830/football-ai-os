$ROOT="E:\football_v"

$LIST="$ROOT\99_DOCUMENTATION\migration\SAFE_DELETE_APPROVAL_LIST_V1.0.csv"

$BACKUP="$ROOT\99_DOCUMENTATION\migration\delete_backup"

$LOG="$ROOT\99_DOCUMENTATION\migration\DELETE_EXECUTION_LOG_V1.0.txt"


New-Item -ItemType Directory -Force $BACKUP | Out-Null


"Football AI OS Safe Delete Log V1.0" | Out-File $LOG -Encoding UTF8

"Time: $(Get-Date)" | Out-File $LOG -Append -Encoding UTF8

"=================================" | Out-File $LOG -Append -Encoding UTF8



if (!(Test-Path $LIST)) {

    Write-Host "ERROR: Approval list missing"

    exit

}



$items=Import-Csv $LIST



foreach($item in $items){


    if($item.delete_status -ne "APPROVED_DELETE"){

        continue

    }


    $file=$item.file

    $target=Join-Path $ROOT $file


    if(Test-Path $target){


        $backupFile=Join-Path $BACKUP $file


        $backupDir=Split-Path $backupFile


        New-Item -ItemType Directory -Force $backupDir | Out-Null



        Copy-Item $target $backupFile -Force



        Remove-Item $target -Force



        "[DELETED] $file" | Out-File $LOG -Append -Encoding UTF8


    }

    else{


        "[MISSING] $file" | Out-File $LOG -Append -Encoding UTF8


    }

}



"完成" | Out-File $LOG -Append -Encoding UTF8

Write-Host "Safe Delete Finished"

Write-Host "Log:"
Write-Host $LOG
