import sqlite3
import os
import sys
from datetime import datetime


# 保证项目根目录可以加载
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)


from config.database_config import SQLITE_DB





def create_retry_policy_table(cursor):

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS retry_policy
        (

            id INTEGER PRIMARY KEY AUTOINCREMENT,


            task_type TEXT UNIQUE,


            max_retry INTEGER DEFAULT 3,


            retry_interval INTEGER DEFAULT 60,


            priority INTEGER DEFAULT 5,


            description TEXT,


            created_time TEXT


        )
        """
    )





def create_task_history_table(cursor):

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS task_history
        (

            id INTEGER PRIMARY KEY AUTOINCREMENT,


            task_id TEXT,


            old_status TEXT,


            new_status TEXT,


            message TEXT,


            created_time TEXT


        )
        """
    )





def create_retry_records_table(cursor):

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS retry_records
        (

            id INTEGER PRIMARY KEY AUTOINCREMENT,


            task_id TEXT,


            attempt INTEGER,


            result TEXT,


            error_message TEXT,


            duration INTEGER,


            created_time TEXT


        )
        """
    )







def init_database():


    print(
        "======================"
    )

    print(
        "Task Reliability Database Init"
    )

    print(
        "======================"
    )


    conn = sqlite3.connect(
        SQLITE_DB
    )


    cursor = conn.cursor()



    create_retry_policy_table(
        cursor
    )


    create_task_history_table(
        cursor
    )


    create_retry_records_table(
        cursor
    )



    conn.commit()


    conn.close()



    print(
        "Retry Policy Table Ready"
    )

    print(
        "Task History Table Ready"
    )

    print(
        "Retry Records Table Ready"
    )


    print(
        "Database Upgrade Completed"
    )





if __name__ == "__main__":

    init_database()