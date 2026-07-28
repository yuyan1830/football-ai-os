import sqlite3


DB=r"E:\football\data\football.db"


conn=sqlite3.connect(DB)

cur=conn.cursor()


print("="*60)
print("OLD SYSTEM HISTORY CHECK")
print("="*60)


cur.execute(
"SELECT name FROM sqlite_master WHERE type='table'"
)


tables=[x[0] for x in cur.fetchall()]


for t in tables:

    if "history" in t.lower() or "rating" in t.lower():

        print(t)


conn.close()

