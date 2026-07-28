# -*- coding: utf-8 -*-

import os


BASE=r"E:\football_v\16_DATABASE_GOVERNANCE_LAYER"


TARGET=os.path.join(
    BASE,
    "backup_engine"
)


os.makedirs(
    TARGET,
    exist_ok=True
)


content=r'''
# -*- coding: utf-8 -*-

import os
import shutil
from datetime import datetime


SOURCE=r"E:\football_v\database"


BACKUP=r"E:\football_v\backup"



def run():

    folder=datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    target=os.path.join(
        BACKUP,
        folder
    )


    os.makedirs(
        target,
        exist_ok=True
    )


    count=0


    if os.path.exists(SOURCE):

        for f in os.listdir(SOURCE):

            if f.endswith(".db"):

                shutil.copy2(

                    os.path.join(
                        SOURCE,
                        f
                    ),

                    target

                )

                count+=1



    print({

        "module":
        "Backup Engine",

        "status":
        "BACKUP_COMPLETE",

        "files":
        count

    })


if __name__=="__main__":

    run()

'''


with open(
os.path.join(
TARGET,
"backup_engine_V1.0.py"
),
"w",
encoding="utf-8"
) as f:

    f.write(content)


print(
{
"module":"Backup Engine",
"status":"CREATED"
}
)

