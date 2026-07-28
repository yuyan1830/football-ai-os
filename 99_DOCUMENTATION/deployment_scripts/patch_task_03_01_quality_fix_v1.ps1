# Football AI OS
# Quality Engine Fix Patch V1


$file="E:\football_v\03_Data_Governance\quality\quality_engine.py"


$content=Get-Content $file -Raw -Encoding UTF8


$content=$content.Replace(
'"service":',
'"module":"03_DATA_GOVERNANCE",`n`n            "service":'
)


$content=$content.Replace(
'"quality_report.json"',
'"E:\\football_v\\03_Data_Governance\\reports\\quality_report.json"'
)


Set-Content `
$file `
$content `
-Encoding UTF8



Write-Host "Quality Engine Patch Completed"

