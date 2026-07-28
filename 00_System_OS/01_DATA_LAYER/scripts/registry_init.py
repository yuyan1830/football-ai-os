import sqlite3
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


def init_registry_tables():


    conn = get_connection()

    cursor = conn.cursor()



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_registry
    (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        data_id TEXT UNIQUE,

        file_name TEXT,

        file_hash TEXT,

        data_type TEXT,

        source TEXT,

        version TEXT,

        status TEXT,

        created_time TEXT

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_lineage
    (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        data_id TEXT,

        parent_data TEXT,

        process TEXT,

        created_time TEXT

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS import_history
    (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        data_id TEXT,

        import_type TEXT,

        operator TEXT,

        import_time TEXT,

        result TEXT

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data_quality
    (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        data_id TEXT,

        completeness REAL,

        accuracy REAL,

        quality_status TEXT

    )
    """)



    conn.commit()

    conn.close()



    print(
        "Registry Tables Ready"
    )



if __name__=="__main__":

    init_registry_tables()