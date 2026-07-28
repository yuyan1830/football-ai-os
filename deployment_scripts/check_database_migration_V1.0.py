import sqlite3
import os
import hashlib

db_old = r"E:\football_v\01_DATA_LAYER\database\match_data.db"
db_new = r"E:\football_v\00_SYSTEM_OS\01_DATA_LAYER\database\match_data.db"

print("="*60)
print("Football AI OS Database Migration Check")
print("="*60)

def scan_db(path):

    data={}

    data["exists"]=os.path.exists(path)

    if not data["exists"]:
        return data

    data["size"]=os.path.getsize(path)

    with sqlite3.connect(path) as conn:

        cur=conn.cursor()

        tables=cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()

        data["tables"]=[x[0] for x in tables]

        data["counts"]={}

        for t in data["tables"]:
            try:
                data["counts"][t]=cur.execute(
                    f"SELECT COUNT(*) FROM '{t}'"
                ).fetchone()[0]
            except:
                data["counts"][t]="ERROR"


    sha=hashlib.sha256()

    with open(path,"rb") as f:
        sha.update(f.read())

    data["sha256"]=sha.hexdigest()

    return data



old=scan_db(db_old)
new=scan_db(db_new)


print("\nOLD DATABASE")
print(db_old)
print(old)


print("\nNEW DATABASE")
print(db_new)
print(new)


print("\nTABLE CHECK")
print("-"*60)

if old.get("tables")==new.get("tables"):
    print("PASS: table structure identical")
else:
    print("FAIL: table structure different")


print("\nROW COUNT CHECK")
print("-"*60)


tables=set(old.get("counts",{})) | set(new.get("counts",{}))


for t in sorted(tables):

    a=old.get("counts",{}).get(t)

    b=new.get("counts",{}).get(t)

    if a==b:
        print("PASS",t,a)

    else:
        print("FAIL",t,"OLD=",a,"NEW=",b)


print("\nDATABASE CHECK COMPLETE")

