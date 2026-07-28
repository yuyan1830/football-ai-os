import sqlite3


DB = r"E:\football\Football_AI_System\data\football.db"


TABLES = [
    "elo_history",
    "dixon_coles_history",
    "poisson_history",
    "team_form_history",
    "fatigue_history",
    "home_away_history",
    "xg_features_history"
]


conn = sqlite3.connect(DB)
cur = conn.cursor()


print("="*60)
print("Football AI OS Ω+ V3.2")
print("LEGACY HISTORY TABLE AUDIT")
print("="*60)


for table in TABLES:

    print("\n")
    print("="*50)
    print("TABLE:", table)


    try:

        # 数据量

        cur.execute(
            f"SELECT COUNT(*) FROM {table}"
        )

        count = cur.fetchone()[0]

        print("ROW COUNT:", count)


        # 字段

        cur.execute(
            f"PRAGMA table_info({table})"
        )

        columns = cur.fetchall()


        print("\nCOLUMNS:")

        for c in columns:
            print(
                "-",
                c[1],
                c[2]
            )


        # 最新5条

        print("\nSAMPLE DATA:")

        cur.execute(
            f"SELECT * FROM {table} LIMIT 3"
        )

        rows = cur.fetchall()

        for r in rows:
            print(r)


    except Exception as e:

        print("ERROR:",e)



conn.close()


print("\nAUDIT FINISHED")