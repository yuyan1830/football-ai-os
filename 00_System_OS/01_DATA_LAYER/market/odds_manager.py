import sqlite3
import datetime


DB_PATH = (
r"E:\football_v\00_System_OS\01_DATA_LAYER"
r"\database\football_ai_os.db"
)



def save_odds(

match_id,

bookmaker,

market,

selection,

odds,

handicap=None

):


    conn=sqlite3.connect(
        DB_PATH
    )


    cursor=conn.cursor()



    cursor.execute(
    """

    INSERT INTO market_snapshot

    (

    match_id,

    bookmaker_id,

    market_code,

    selection,

    handicap,

    odds,

    capture_time,

    version

    )


    VALUES

    (?,?,?,?,?,?,?,?)

    """,

    (

    match_id,

    bookmaker,

    market,

    selection,

    handicap,

    odds,

    datetime.datetime.now().isoformat(),

    "v001"

    )

    )


    conn.commit()

    conn.close()



    print(
        "ODDS SAVED"
    )



if __name__=="__main__":


    save_odds(

    "MATCH001",

    "BK1",

    "1X2",

    "HOME",

    2.10

    )


    save_odds(

    "MATCH001",

    "BK1",

    "1X2",

    "DRAW",

    3.40

    )


    save_odds(

    "MATCH001",

    "BK1",

    "1X2",

    "AWAY",

    3.20

    )