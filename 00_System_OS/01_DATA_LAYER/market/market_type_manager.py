import sqlite3


DB_PATH = (
r"E:\football_v\00_System_OS\01_DATA_LAYER"
r"\database\football_ai_os.db"
)



MARKETS=[


("1X2","Win Draw Lose",100),

("HANDICAP","Asian Handicap",100),

("OU","Over Under",90),

("BTTS","Both Teams Score",60),

("CS","Correct Score",40)

]



def init_market_types():


    conn=sqlite3.connect(
        DB_PATH
    )


    cursor=conn.cursor()



    for m in MARKETS:


        cursor.execute(
        """

        INSERT OR IGNORE INTO market_type_registry

        (

        market_code,

        market_name,

        priority

        )


        VALUES

        (?,?,?)

        """,

        m

        )


    conn.commit()

    conn.close()



    print(
        "Market Types Ready"
    )



if __name__=="__main__":

    init_market_types()