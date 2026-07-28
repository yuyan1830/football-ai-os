import sqlite3


DB_PATH = (
r"E:\football_v\00_System_OS\01_DATA_LAYER"
r"\database\football_ai_os.db"
)



def init_market_database():


    conn = sqlite3.connect(
        DB_PATH
    )

    cursor = conn.cursor()


    # 博彩公司

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookmaker_registry
    (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        bookmaker_id TEXT UNIQUE,

        name TEXT,

        market_type TEXT,

        weight REAL,

        quality_score REAL,

        status TEXT

    )
    """)



    # 市场类型

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS market_type_registry
    (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        market_code TEXT UNIQUE,

        market_name TEXT,

        priority INTEGER

    )
    """)



    # 赔率快照

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS market_snapshot
    (

        id INTEGER PRIMARY KEY AUTOINCREMENT,


        match_id TEXT,


        bookmaker_id TEXT,


        market_code TEXT,


        selection TEXT,


        handicap TEXT,


        odds REAL,


        capture_time TEXT,


        version TEXT

    )
    """)



    conn.commit()

    conn.close()


    print(
        "Market Database Initialized"
    )



if __name__=="__main__":

    init_market_database()