
import sqlite3


db=r"E:\football_v\13_TEST_LAYER\runtime\test_runtime.db"


conn=sqlite3.connect(db)

cur=conn.cursor()


print(
cur.execute(
"select name from sqlite_master where type='table'"
).fetchall()
)


print("DATABASE TEST PASS")

