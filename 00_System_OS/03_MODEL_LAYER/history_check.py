import sqlite3


DB=r"E:\football_v\01_DATA_LAYER\database\match_data.db"


conn=sqlite3.connect(DB)

cur=conn.cursor()


tables=[

"elo_history",

"dixon_coles_history",

"poisson_history",

"team_form_history",

"fatigue_history",

"home_away_history"

]


print("="*60)
print("HISTORY TABLE CHECK")
print("="*60)


for t in tables:

    print()
    print("TABLE:",t)

    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
        (t,)
    )

    r=cur.fetchone()

    if r:

        print("[EXIST]")

        cur.execute(
            f"PRAGMA table_info({t})"
        )

        cols=cur.fetchall()

        for c in cols:

            print(" ",c[1])

    else:

        print("[NOT FOUND]")


conn.close()

