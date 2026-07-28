# Football AI OS Recovery Scheduler V1.0


$TaskName = "Football_AI_OS_Recovery"



$PythonPath = `
"C:\Users\admin\AppData\Local\Programs\Python\Python312\python.exe"



$ScriptPath = `
"E:\football_v\00_SYSTEM_OS\Recovery\recovery_controller.py"



$Action = New-ScheduledTaskAction `
-Execute $PythonPath `
-Argument $ScriptPath



$Trigger = New-ScheduledTaskTrigger `
-Daily `
-At 2:10AM



Register-ScheduledTask `
-TaskName $TaskName `
-Action $Action `
-Trigger $Trigger `
-Description `
"Football AI OS Recovery Controller"



Write-Host ""
Write-Host "================================="
Write-Host "Football AI OS Recovery Installed"
Write-Host "Task:"
Write-Host $TaskName
Write-Host "Run Time: Daily 02:10"
Write-Host "================================="