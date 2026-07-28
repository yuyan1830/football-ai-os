# Football AI OS Scheduler Installer V1.0

$TaskName = "Football_AI_OS_Daily_Maintenance"


$PythonPath = "C:\Users\admin\AppData\Local\Programs\Python\Python312\python.exe"


$ScriptPath = "E:\football_v\00_System_OS\Automation\task_manager\task_manager.py"



$Action = New-ScheduledTaskAction `
-Execute $PythonPath `
-Argument $ScriptPath



$Trigger = New-ScheduledTaskTrigger `
-Daily `
-At 2:00AM



Register-ScheduledTask `
-TaskName $TaskName `
-Action $Action `
-Trigger $Trigger `
-Description "Football AI OS Daily Automation"



Write-Host ""
Write-Host "================================="
Write-Host "Football AI OS Scheduler Installed"
Write-Host "Task:"
Write-Host $TaskName
Write-Host "Run Time: Daily 02:00"
Write-Host "================================="