import sqlite3


DB=r"E:\football_v\01_DATA_LAYER\database\match_data.db"


conn=sqlite3.connect(DB)

cur=conn.cursor()


print("="*60)
print("MATCH DATA SOURCE CHECK")
print("="*60)


cur.execute(
"SELECT name FROM sqlite_master WHERE type='table'"
)


for x in cur.fetchall():
    print(x[0])


conn.close()

