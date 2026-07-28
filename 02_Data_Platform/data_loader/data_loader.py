# -*- coding: utf-8 -*-

"""
Football AI OS
Data Loader Engine V1.0
"""

import os
import json
from datetime import datetime


ROOT = os.path.dirname(
    os.path.dirname(__file__)
)

RAW_PATH = os.path.join(
    ROOT,
    "raw"
)


def scan_raw():

    files=[]

    for root,dirs,names in os.walk(RAW_PATH):

        for name in names:

            files.append(
                os.path.join(root,name)
            )

    return files



def load_report():

    data={

        "module":
        "02_DATA_PLATFORM",

        "service":
        "data_loader",

        "version":
        "V1.0",

        "time":
        str(datetime.now()),

        "raw_files":
        scan_raw(),

        "count":
        len(scan_raw())

    }


    return data



if __name__=="__main__":

    print("="*50)

    print(
    "Football AI OS Data Loader V1.0"
    )

    print("="*50)


    print(
        json.dumps(
            load_report(),
            indent=4,
            ensure_ascii=False
        )
    )