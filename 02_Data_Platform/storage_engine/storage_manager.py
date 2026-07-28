# -*- coding: utf-8 -*-

"""
Football AI OS
Storage Manager V1.1
Data Platform Storage Engine
"""

import os
import json
from datetime import datetime


ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


RAW_PATH = os.path.join(
    ROOT,
    "raw"
)


PROCESSED_PATH = os.path.join(
    ROOT,
    "processed"
)


REGISTRY_PATH = os.path.join(
    os.path.dirname(__file__),
    "storage_registry.json"
)


def scan_folder(path):

    result=[]

    if not os.path.exists(path):
        return result


    for root,dirs,files in os.walk(path):

        for f in files:

            result.append(
                {
                    "file":os.path.join(
                        root,
                        f
                    ),
                    "size":os.path.getsize(
                        os.path.join(root,f)
                    )
                }
            )

    return result



def build_registry():


    data={

        "framework":
        "Football AI OS",


        "module":
        "02_DATA_PLATFORM",


        "service":
        "Storage Engine",


        "version":
        "V1.1",


        "time":
        str(datetime.now()),


        "storage":

        {

            "raw":

            scan_folder(
                RAW_PATH
            ),


            "processed":

            scan_folder(
                PROCESSED_PATH
            )

        }

    }


    with open(
        REGISTRY_PATH,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


    return data



if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Storage Manager V1.1"
    )

    print("="*50)


    result=build_registry()


    print(
        "RAW FILES:",
        len(
            result["storage"]["raw"]
        )
    )


    print(
        "PROCESSED FILES:",
        len(
            result["storage"]["processed"]
        )
    )


    print(
        "Registry Created:"
    )


    print(
        REGISTRY_PATH
    )