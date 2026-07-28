import sqlite3


DATABASES={

"match":
r"E:\football_v\01_DATA_LAYER\database\match_data.db",

"feature":
r"E:\football_v\02_FEATURE_LAYER\database\feature_store.db",

"model":
r"E:\football_v\03_MODEL_LAYER\database\model_store.db"

}


def check_database():

    result={}

    for name,path in DATABASES.items():

        try:

            conn=sqlite3.connect(path)

            conn.close()

            result[name]="ONLINE"


        except Exception:

            result[name]="OFFLINE"


    return result



def get_tables(db):

    path=DATABASES.get(db)

    conn=sqlite3.connect(path)

    cursor=conn.cursor()

    tables=cursor.execute(
        "select name from sqlite_master where type='table'"
    ).fetchall()

    conn.close()

    return tables

