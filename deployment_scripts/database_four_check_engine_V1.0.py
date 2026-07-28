import os
import sqlite3
import json
import hashlib
from datetime import datetime


BASE = r"E:\football_v"


DATABASES = {

    "football_ai_os":
    r"E:\football_v\00_SYSTEM_OS\01_DATA_LAYER\database\football_ai_os.db",

    "match_data":
    r"E:\football_v\00_SYSTEM_OS\01_DATA_LAYER\database\match_data.db",

    "feature_store":
    r"E:\football_v\00_SYSTEM_OS\02_FEATURE_LAYER\database\feature_store.db",

    "model_store":
    r"E:\football_v\00_SYSTEM_OS\03_MODEL_LAYER\database\model_store.db"

}


REPORT = r"E:\football_v\99_Documentation\reports\DATABASE_FOUR_CHECK_REPORT_V1.0.json"



def sha256(path):

    h = hashlib.sha256()

    with open(path,"rb") as f:

        for data in iter(lambda:f.read(1024*1024),b""):

            h.update(data)

    return h.hexdigest()



def check_database(name,path):

    result = {

        "name":name,
        "path":path,
        "exists":False,
        "size":0,
        "sha256":None,
        "tables":{},
        "status":"FAIL"

    }


    if not os.path.exists(path):

        return result



    result["exists"]=True

    result["size"]=os.path.getsize(path)

    result["sha256"]=sha256(path)



    conn=sqlite3.connect(path)

    cur=conn.cursor()



    tables=cur.execute(

        """
        SELECT name 
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name
        """

    ).fetchall()



    for t in tables:

        table=t[0]


        if table=="sqlite_sequence":

            continue


        try:

            count=cur.execute(

                f"SELECT COUNT(*) FROM [{table}]"

            ).fetchone()[0]


            result["tables"][table]=count


        except Exception as e:

            result["tables"][table]=str(e)



    conn.close()


    result["status"]="PASS"


    return result



def main():

    print("="*60)

    print("Football AI OS Four Database Check V1.0")

    print("="*60)



    report={

        "version":"DATABASE_FOUR_CHECK_V1.0",

        "time":datetime.now().isoformat(),

        "databases":{}

    }



    for name,path in DATABASES.items():

        print()

        print("Checking:",name)


        result=check_database(

            name,

            path

        )


        report["databases"][name]=result


        print(

            result["status"],

            path

        )


        if result["exists"]:

            print(

                "Tables:",

                len(result["tables"])

            )



    os.makedirs(

        os.path.dirname(REPORT),

        exist_ok=True

    )


    with open(

        REPORT,

        "w",

        encoding="utf-8"

    ) as f:


        json.dump(

            report,

            f,

            indent=4,

            ensure_ascii=False

        )


    print()

    print("="*60)

    print("CHECK COMPLETE")

    print(REPORT)

    print("="*60)



if __name__=="__main__":

    main()

