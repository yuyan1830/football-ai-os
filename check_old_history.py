import sqlite3


dbs = [

r"E:\football\Football_AI_System\data\football.db",

r"E:\football\Football_AI_System\02_Database\football.db"

]


keywords=[
"history",
"form",
"fatigue",
"elo",
"poisson",
"dixon",
"home",
"away",
"rating"
]


for db in dbs:

    print("\n==============================")
    print(db)

    try:

        conn=sqlite3.connect(db)

        cur=conn.cursor()

        cur.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            """
        )

        tables=[
            x[0]
            for x in cur.fetchall()
        ]


        print("TABLE COUNT:",len(tables))


        for t in tables:

            print(t)

        print("\n---- HISTORY RELATED ----")


        for t in tables:

            low=t.lower()

            if any(k in low for k in keywords):

                print("FOUND:",t)


        conn.close()


    except Exception as e:

        print("ERROR:",e)