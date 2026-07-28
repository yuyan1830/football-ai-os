import os
import json
import datetime


ROOT=r"E:\FOOTBALL_V"


result={

    "version":
    "DATABASE_LOCATION_DISCOVERY_V4.0",

    "time":
    str(datetime.datetime.now()),

    "databases":[]

}


for root,dirs,files in os.walk(ROOT):

    for file in files:

        if file.lower().endswith(".db"):

            path=os.path.join(root,file)

            result["databases"].append(path)

            print(path)



out=r"E:\FOOTBALL_V\99_DOCUMENTATION\MODEL_DATA_SNAPSHOT_V4.0\DATABASE_LOCATION_V4.0.json"


with open(
    out,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        indent=4,
        ensure_ascii=False
    )


print()

print("="*60)

print("DATABASE DISCOVERY COMPLETE")

print("Found:",len(result["databases"]))

print(out)

print("="*60)

