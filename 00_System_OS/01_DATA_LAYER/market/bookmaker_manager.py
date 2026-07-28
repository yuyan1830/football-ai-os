import sqlite3



DB_PATH = (
r"E:\football_v\00_System_OS\01_DATA_LAYER"
r"\database\football_ai_os.db"
)



BOOKMAKERS = [


{
"name":"Pinnacle",
"type":"Sharp",
"weight":1.0,
"quality":0.95
},


{
"name":"Betfair",
"type":"Exchange",
"weight":0.95,
"quality":0.90
},


{
"name":"SBO",
"type":"Asian",
"weight":0.90,
"quality":0.90
},


{
"name":"Bet365",
"type":"Public",
"weight":0.85,
"quality":0.85
}


]



def register_bookmakers():


    conn=sqlite3.connect(
        DB_PATH
    )

    cursor=conn.cursor()


    for i,bk in enumerate(
        BOOKMAKERS
    ):


        cursor.execute(
        """

        INSERT OR IGNORE INTO bookmaker_registry

        (

        bookmaker_id,

        name,

        market_type,

        weight,

        quality_score,

        status

        )


        VALUES

        (?,?,?,?,?,?)

        """,

        (

        "BK"+str(i+1),

        bk["name"],

        bk["type"],

        bk["weight"],

        bk["quality"],

        "active"

        )


        )


    conn.commit()

    conn.close()


    print(
        "Bookmakers Registered"
    )



if __name__=="__main__":

    register_bookmakers()