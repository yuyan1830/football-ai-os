# -*- coding: utf-8 -*-

import os


BASE=r"E:\football_v\16_DATABASE_GOVERNANCE_LAYER"


TARGET=os.path.join(
    BASE,
    "restore_engine"
)


os.makedirs(
    TARGET,
    exist_ok=True
)


content=r'''
# -*- coding: utf-8 -*-

import os
import shutil
import json
from datetime import datetime


BACKUP=r"E:\football_v\backup"

DATABASE=r"E:\football_v\database"



def run():

    result={

        "module":
        "Restore Engine",

        "version":
        "V1.0",

        "status":
        "NO_BACKUP"

    }


    if not os.path.exists(BACKUP):

        print(result)

        return



    backups=os.listdir(BACKUP)


    if len(backups)==0:

        print(result)

        return



    latest=sorted(backups)[-1]


    source=os.path.join(
        BACKUP,
        latest
    )


    os.makedirs(
        DATABASE,
        exist_ok=True
    )


    count=0


    for file in os.listdir(source):

        if file.endswith(".db"):

            shutil.copy2(

                os.path.join(
                    source,
                    file
                ),

                os.path.join(
                    DATABASE,
                    file
                )

            )

            count+=1



    result={

        "module":
        "Restore Engine",

        "version":
        "V1.0",

        "status":
        "RESTORE_COMPLETE",

        "files":
        count,

        "time":
        str(datetime.now())

    }


    with open(

        r"E:\football_v\16_DATABASE_GOVERNANCE_LAYER\restore_engine\restore_report.json",

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(
            result,
            f,
            indent=4,
            ensure_ascii=False
        )


    print(result)



if __name__=="__main__":

    run()

'''


with open(

os.path.join(
TARGET,
"restore_engine_V1.0.py"
),

"w",

encoding="utf-8"

) as f:

    f.write(content)



print({

"module":
"Restore Engine",

"status":
"CREATED"

})

