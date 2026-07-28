# Football AI OS V1.0
# Project Structure Initialization


$Root = "E:\football_v"


$Folders = @(

"00_System_OS",
"00_System_OS\core",
"00_System_OS\config",
"00_System_OS\logs",
"00_System_OS\runtime",
"00_System_OS\registry",
"00_System_OS\services",

"01_Data_Source",
"01_Data_Source\registry",
"01_Data_Source\download",
"01_Data_Source\monitor",

"02_Data_Platform",
"02_Data_Platform\raw",
"02_Data_Platform\processed",
"02_Data_Platform\archive",

"03_Data_Governance",
"03_Data_Governance\quality",
"03_Data_Governance\lineage",

"04_Data_Processing_AI",

"05_Master_Data",

"06_Feature_Store",

"07_Model_Engine",
"07_Model_Engine\models",
"07_Model_Engine\training",

"08_Model_Registry",

"09_Prediction_System",

"10_Dashboard",

"11_System_Intelligence",

"Database",
"Database\PostgreSQL",
"Database\MinIO",

"Storage",

"Logs",

"Config",

"Scripts",

"Documentation"

)



foreach ($folder in $Folders)
{

    $Path = Join-Path $Root $folder

    if (!(Test-Path $Path))
    {
        New-Item -ItemType Directory -Path $Path | Out-Null
    }

}



$Files = @(

"00_System_OS\runtime\system_state.json",

"00_System_OS\registry\module_registry.json",

"Config\system_version.yaml",

"Documentation\README.md",

"Logs\system.log"

)



foreach ($file in $Files)
{

    $FilePath = Join-Path $Root $file

    if (!(Test-Path $FilePath))
    {
        New-Item -ItemType File -Path $FilePath | Out-Null
    }

}



Write-Host "Football AI OS V1.0 initialization finished"