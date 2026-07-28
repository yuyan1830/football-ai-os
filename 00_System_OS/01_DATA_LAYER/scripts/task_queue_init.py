import os
import sys


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(
    0,
    BASE_DIR
)


from core.db_connection import get_connection



def init_task_table():


    conn=get_connection()

    cursor=conn.cursor()



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_tasks
    (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        task_id TEXT UNIQUE,

        task_type TEXT,

        source TEXT,

        target TEXT,

        status TEXT,

        priority INTEGER,

        error_message TEXT,

        created_time TEXT,

        updated_time TEXT

    )
    """)



    conn.commit()

    conn.close()


    print(
        "Task Queue Table Ready"
    )



if __name__=="__main__":

    init_task_table()