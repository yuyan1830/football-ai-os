import sqlite3
import os


DB_PATH = (
r"E:\football_v\00_System_OS\01_DATA_LAYER"
r"\database\football_ai_os.db"
)


def create_database():

    os.makedirs(
        os.path.dirname(DB_PATH),
        exist_ok=True
    )


    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    # 数据注册表

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_registry
    (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        data_id TEXT UNIQUE,

        file_name TEXT,

        file_path TEXT,

        data_type TEXT,

        source TEXT,

        hash TEXT,

        version TEXT,

        status TEXT,

        created_time TEXT

    )
    """)



    # 文件版本

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS file_version
    (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        file_name TEXT,

        version TEXT,

        hash TEXT,

        created_time TEXT

    )
    """)



    # 审计日志

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_log
    (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        action TEXT,

        target TEXT,

        result TEXT,

        created_time TEXT

    )
    """)



    conn.commit()

    conn.close()


    print(
        "Football AI OS Database Initialized"
    )


if __name__ == "__main__":

    create_database()