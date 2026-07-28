import os
import shutil
import hashlib
import json
from datetime import datetime


BASE = r"E:\football_v"


OLD_DB = os.path.join(
    BASE,
    "database",
    "football_ai_os.db"
)


NEW_DB = os.path.join(
    BASE,
    "00_SYSTEM_OS",
    "01_DATA_LAYER",
    "database",
    "football_ai_os.db"
)


REPORT = os.path.join(
    BASE,
    "99_Documentation",
    "reports",
    "DATABASE_SYSTEM_DB_MIGRATION_V2.2.2_REPORT.json"
)



def sha256(path):

    h = hashlib.sha256()

    with open(path,"rb") as f:

        for chunk in iter(
            lambda:f.read(1024*1024),
            b""
        ):

            h.update(chunk)

    return h.hexdigest()



def main():

    print("="*60)
    print("Football AI OS System Database Migration V2.2.2")
    print("="*60)


    report = {

        "version":
        "DATABASE_SYSTEM_DB_MIGRATION_V2.2.2",

        "time":
        datetime.now().isoformat(),

        "old_database":
        OLD_DB,

        "new_database":
        NEW_DB,

        "status":
        "FAIL"

    }



    if not os.path.exists(OLD_DB):

        print(
            "OLD DATABASE NOT FOUND"
        )

        report["reason"]="old database missing"


    else:

        print(
            "Found:",
            OLD_DB
        )


        os.makedirs(
            os.path.dirname(NEW_DB),
            exist_ok=True
        )


        print(
            "Copying..."
        )


        shutil.copy2(
            OLD_DB,
            NEW_DB
        )


        old_hash=sha256(OLD_DB)

        new_hash=sha256(NEW_DB)



        report["old_sha256"]=old_hash

        report["new_sha256"]=new_hash



        if old_hash==new_hash:

            report["status"]="PASS"

            print(
                "SHA256 CHECK PASS"
            )


        else:

            report["status"]="FAIL"

            print(
                "SHA256 CHECK FAIL"
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
    print(
        "Migration Complete"
    )
    print(
        REPORT
    )
    print("="*60)



if __name__=="__main__":

    main()

