# ==========================================================
# Football AI OS Ω+ V3.2.2
# AI Agent Environment Setup
# Version: V1.0
#
# Purpose:
# Prepare Claude Code + Continue AI Agent environment
#
# Does NOT modify:
# - Model Layer
# - Database
# - Architecture
# - Source Code
#
# ==========================================================


$ProjectRoot = "E:\football_v"


Write-Host ""
Write-Host "========================================"
Write-Host " Football AI OS Ω+ V3.2.2"
Write-Host " AI Agent Environment Setup"
Write-Host "========================================"
Write-Host ""


# ==========================================================
# 1. Create required directories
# ==========================================================


$Directories = @(

    "$ProjectRoot\.claude",

    "$ProjectRoot\.continue",

    "$ProjectRoot\.continue\rules",

    "$ProjectRoot\99_DOCUMENTATION\validation",

    "$ProjectRoot\tools"

)


foreach ($dir in $Directories) {

    if (!(Test-Path $dir)) {

        New-Item -ItemType Directory -Path $dir | Out-Null

        Write-Host "[CREATE] $dir"

    }
    else {

        Write-Host "[EXISTS] $dir"

    }

}



# ==========================================================
# 2. Create Claude Code local settings
# ==========================================================


$ClaudeSettings = @"
{
  "permissions": {
    "allow": [
      "Read",
      "Search",
      "Git"
    ],
    "deny": [
      "Delete",
      "DatabaseSchemaChange"
    ]
  },

  "project": {
    "name": "Football AI OS Ω+ V3.2.2",
    "mode": "Runtime Stabilization"
  }
}
"@


$ClaudeFile =
"$ProjectRoot\.claude\settings.local.json"


if (!(Test-Path $ClaudeFile)) {

    $ClaudeSettings | Out-File `
    -Encoding UTF8 `
    $ClaudeFile

    Write-Host "[CREATE] Claude Code settings"

}
else {

    Write-Host "[EXISTS] Claude Code settings"

}



# ==========================================================
# 3. Create Continue rules
# ==========================================================


$ContinueRules = @"
# Football AI OS Ω+ V3.2.2
# Continue AI Rules


Project:

Football AI OS Betting Intelligence System Ω+


Current Version:

V3.2.2


Current Task:

Runtime Stabilization


Before code modification:


1. Read CLAUDE.md

2. Check Omega V3.2 Baseline

3. Check Legacy Asset Index

4. Analyze impact


Forbidden:


- Create new MODEL_LAYER

- Delete Legacy assets

- Redesign architecture

- Change model formulas

- Modify database blindly


Production Model Layer:


E:\football_v\05_MODEL_AI\MODEL_LAYER


Legacy Reference:


E:\football_v\00_System_OS\03_MODEL_LAYER


Workflow:


Scan

↓

Report

↓

Review

↓

Modify

↓

Test

↓

Commit


"@


$ContinueFile =
"$ProjectRoot\.continue\rules\FOOTBALL_AI_OS_RULES.md"


if (!(Test-Path $ContinueFile)) {

    $ContinueRules | Out-File `
    -Encoding UTF8 `
    $ContinueFile

    Write-Host "[CREATE] Continue rules"

}
else {

    Write-Host "[EXISTS] Continue rules"

}



# ==========================================================
# 4. Create validation placeholder
# ==========================================================


$Readme =
@"
# Football AI OS Ω+ V3.2.2 Validation

AI Agent scan reports are stored here.

Example:

V3.2.2_RUNTIME_SCAN_REPORT.md

"@


$ValidationFile =
"$ProjectRoot\99_DOCUMENTATION\validation\README.md"


if (!(Test-Path $ValidationFile)) {

    $Readme | Out-File `
    -Encoding UTF8 `
    $ValidationFile

    Write-Host "[CREATE] Validation folder"

}



# ==========================================================
# 5. Environment check
# ==========================================================


Write-Host ""
Write-Host "========================================"
Write-Host " Environment Check"
Write-Host "========================================"


$Checks = @(

    ".claude",

    ".continue",

    ".continue\rules",

    "99_DOCUMENTATION\validation",

    "CLAUDE.md"

)


foreach ($item in $Checks) {


    $path = Join-Path $ProjectRoot $item


    if (Test-Path $path) {

        Write-Host "[PASS] $item"

    }
    else {

        Write-Host "[FAIL] $item"

    }

}



Write-Host ""
Write-Host "========================================"
Write-Host " AI Agent Environment Ready"
Write-Host " Next Step:"
Write-Host " Run Claude Code Runtime Stabilization Scan"
Write-Host "========================================"
