
import sqlite3


db=r'E:\football_v\09_APPLICATION_LAYER\runtime\application_runtime.db'


conn=sqlite3.connect(db)


print("TABLES")


for x in conn.execute(

"select name from sqlite_master where type='table'"

):

    print(x[0])



print("")


print("REGISTRY COUNT")


print(

conn.execute(

"select count(*) from application_registry"

).fetchone()[0]

)



conn.close()

