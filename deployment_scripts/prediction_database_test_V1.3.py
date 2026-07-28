import sqlite3

db=r"E:\football_v\04_PREDICTION_LAYER\database\prediction_service.db"

conn=sqlite3.connect(db)

cur=conn.cursor()


print("TABLES")

for x in cur.execute(
"SELECT name FROM sqlite_master WHERE type='table'"
):

    print(x[0])


print("")
print("COUNTS")


for t in [
"prediction_history",
"probability_fusion",
"prediction_result",
"prediction_audit"
]:

    print(
        t,
        cur.execute(
        f"SELECT COUNT(*) FROM {t}"
        ).fetchone()[0]
    )


conn.close()

