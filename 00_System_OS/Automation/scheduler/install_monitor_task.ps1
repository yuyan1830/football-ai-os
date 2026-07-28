# Football AI OS Monitor Scheduler V1.0


$TaskName = "Football_AI_OS_Monitor"


$PythonPath = `
"C:\Users\admin\AppData\Local\Programs\Python\Python312\python.exe"


$ScriptPath = `
"E:\football_v\00_System_OS\Monitor\monitor_service.py"



$Action = New-ScheduledTaskAction `
-Execute $PythonPath `
-Argument $ScriptPath



$Trigger = New-ScheduledTaskTrigger `
-Daily `
-At 2:05AM



Register-ScheduledTask `
-TaskName $TaskName `
-Action $Action `
-Trigger $Trigger `
-Description `
"Football AI OS Monitor Service"



Write-Host ""
Write-Host "Football AI OS Monitor Installed"
Write-Host $TaskName