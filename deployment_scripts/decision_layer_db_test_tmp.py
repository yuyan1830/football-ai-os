
import sqlite3


db=r'E:\football_v\08_DECISION_LAYER\database\decision_history.db'


conn=sqlite3.connect(db)


print("TABLES")


for x in conn.execute(

"select name from sqlite_master where type='table'"

):

    print(x[0])


print("")


print("COUNTS")


for t in [

"decision_history",

"decision_registry"

]:


    try:

        c=conn.execute(

        f"select count(*) from {t}"

        ).fetchone()[0]


        print(t,c)


    except Exception as e:

        print(t,"ERROR")


conn.close()

