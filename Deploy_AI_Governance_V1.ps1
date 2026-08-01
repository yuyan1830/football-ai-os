# ==================================================
# Football AI OS Ω+
# AI Governance Layer V1.0 Deployment
# Version: V1.0
# ==================================================

$ROOT="E:\football_v"

$BACKUP="$ROOT\99_DOCUMENTATION\backup\AI_GOVERNANCE_BACKUP"

$ARCHIVE="$ROOT\99_DOCUMENTATION\archive\AI_GOVERNANCE_LEGACY"

$CHECKPOINT="$ROOT\99_DOCUMENTATION\checkpoints"


Write-Host "================================="
Write-Host "Football AI OS Governance Deploy"
Write-Host "================================="


# -----------------------------
# 1. 创建目录
# -----------------------------

New-Item `
-ItemType Directory `
-Force `
$BACKUP | Out-Null


New-Item `
-ItemType Directory `
-Force `
$ARCHIVE | Out-Null



# -----------------------------
# 2. 备份现有治理文件
# -----------------------------

Write-Host "Backup current governance files..."


Copy-Item `
"$ROOT\CLAUDE.md" `
$BACKUP `
-Force



Copy-Item `
"$ROOT\.claude" `
$BACKUP `
-Recurse `
-Force



Copy-Item `
"$ROOT\.continue\rules" `
$BACKUP `
-Recurse `
-Force



# -----------------------------
# 3. 归档旧规则
# -----------------------------


Write-Host "Archive legacy rules..."


$LegacyFiles=@(

"$ROOT\.continue\rules\DEVELOPMENT_WORKFLOW_V4.md",

"$ROOT\.continue\rules\FOOTBALL_AI_OS_GOVERNANCE.md",

"$ROOT\.continue\rules\project.md"

)



foreach($file in $LegacyFiles)
{

if(Test-Path $file)
{

Move-Item `
$file `
$ARCHIVE `
-Force

}

}



# -----------------------------
# 4. 创建Checkpoint
# -----------------------------


$checkpointFile="$CHECKPOINT\Checkpoint-071_AI_Governance_Consolidation.txt"



@"

==================================================
Football AI OS Ω+

Checkpoint-071

AI Governance Layer Consolidation

==================================================


Status:

COMPLETED



Completed:


1.
CLAUDE governance structure reviewed


2.
Claude Code governance consolidated


3.
Continue governance consolidated


4.
Duplicate governance files archived


5.
AI development hierarchy established



Final Structure:


CLAUDE.md

↓

Claude Code Governance

↓

Continue Development Rules



Current Version:


AI Governance Layer V1.0



Next Phase:


V3.2 Final Architecture Audit



==================================================

"@ | Set-Content `
$checkpointFile `
-Encoding UTF8



# -----------------------------
# 5. Git检查
# -----------------------------


Write-Host ""
Write-Host "Deployment completed."
Write-Host ""
Write-Host "Run:"
Write-Host ""
Write-Host "git status"
Write-Host ""
Write-Host "then commit changes."
