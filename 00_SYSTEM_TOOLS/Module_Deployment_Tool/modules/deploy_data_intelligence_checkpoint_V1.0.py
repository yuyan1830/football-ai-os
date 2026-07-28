# -*- coding: utf-8 -*-

import os
import json
from datetime import datetime


CHECKPOINT_DIR = r"E:\football_v\99_Documentation\checkpoints"


os.makedirs(
    CHECKPOINT_DIR,
    exist_ok=True
)


checkpoint={


    "framework":

    "Football AI OS Ultimate Fusion Framework V1.5",


    "module":

    "04_DATA_PROCESSING_AI",


    "service":

    "Data Intelligence Engine",


    "version":

    "V1.0",


    "status":

    "PASS",


    "dependencies":

    [

        "Feature Store V1.0",

        "Cleaning Engine",

        "Transformation Engine",

        "Feature Engine"

    ],


    "supported_models":

    [

        "Elo",

        "Dixon-Coles",

        "Poisson",

        "XGBoost",

        "Fusion"

    ],


    "time":

    str(datetime.now())

}



path=os.path.join(

    CHECKPOINT_DIR,

    "Football_AI_OS_Data_Intelligence_Engine_V1.0_Checkpoint.json"

)


with open(

    path,

    "w",

    encoding="utf-8"

) as f:


    json.dump(

        checkpoint,

        f,

        indent=4,

        ensure_ascii=False

    )


print("="*60)

print(json.dumps(

    checkpoint,

    indent=4,

    ensure_ascii=False

))


print("="*60)