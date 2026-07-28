Write-Host "====================================="
Write-Host "Football AI OS"
Write-Host "Database Service V1.1 Upgrade"
Write-Host "====================================="


$CORE_PATH="E:\football_v\00_System_OS\01_DATA_LAYER\core"

$DB_FILE="$CORE_PATH\db_connection.py"


$BACKUP_DIR="E:\football_v\99_DOCUMENTATION\checkpoints\database_backup_v11"


$CHECKPOINT="E:\football_v\99_DOCUMENTATION\checkpoints\Checkpoint-023_Database_Service_V1.1_Stable.txt"



# =========================
# Backup
# =========================

if (!(Test-Path $BACKUP_DIR)) {

New-Item `
-ItemType Directory `
-Path $BACKUP_DIR `
-Force | Out-Null

}


Copy-Item `
$DB_FILE `
"$BACKUP_DIR\db_connection_backup.py" `
-Force



Write-Host ""
Write-Host "Database backup completed"



# =========================
# Write new db_connection.py
# =========================


@'

import sqlite3
import sys
import os



BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)



if BASE_DIR not in sys.path:

    sys.path.insert(
        0,
        BASE_DIR
    )



from config.database_config import SQLITE_DB



# Logger integration

try:

    from core.logger import logger

except:

    logger = None



# Exception integration

try:

    from core.exception import DatabaseException

except:

    class DatabaseException(Exception):
        pass





def get_connection():


    try:


        conn = sqlite3.connect(

            SQLITE_DB,

            timeout=30

        )


        return conn



    except sqlite3.Error as e:


        if logger:

            logger.error(
                str(e)
            )


        raise DatabaseException(
            str(e)
        )






def test_connection():


    conn=None


    try:


        conn=get_connection()


        cursor=conn.cursor()


        cursor.execute(

            "SELECT sqlite_version();"

        )


        result=cursor.fetchone()


        return result



    except Exception as e:


        if logger:

            logger.error(
                str(e)
            )


        raise



    finally:


        if conn:

            conn.close()






def health_check():


    result=test_connection()


    return {


        "service":
            "Database Service",


        "status":
            "OK",


        "sqlite_version":
            result[0]

    }





if __name__=="__main__":


    print(
        health_check()
    )


'@ | Out-File `
$DB_FILE `
-Encoding UTF8




Write-Host ""
Write-Host "Database Service upgraded"




# =========================
# Checkpoint
# =========================


@'

Football AI OS

Checkpoint-023


Module:

Database Service


Version:

V1.1


Upgrade:

1. Backup old db_connection.py

2. Logger integration

3. Exception integration

4. Connection timeout

5. Health check added



Interface:

Compatible


Test:

SQLite connection


Status:

Stable


'@ | Out-File `
$CHECKPOINT `
-Encoding UTF8




Write-Host ""
Write-Host "Checkpoint Created:"
Write-Host $CHECKPOINT



# =========================
# Test
# =========================


Write-Host ""
Write-Host "Testing Database Service..."



python $DB_FILE



Write-Host ""
Write-Host "Database Service V1.1 Completed"
