# -*- coding: utf-8 -*-

"""
Football AI OS
Loader Engine V1.0
"""

import os
import json
from datetime import datetime


class LoaderEngine:


    def __init__(self):

        self.raw_path = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)
                )
            ),
            "raw"
        )


    def scan(self):

        files=[]

        for root,dirs,names in os.walk(
            self.raw_path
        ):

            for name in names:

                files.append(
                    os.path.join(
                        root,
                        name
                    )
                )

        return files



    def report(self):

        return {

            "module":
            "02_DATA_PLATFORM",

            "service":
            "loader_engine",

            "version":
            "V1.0",

            "status":
            "active",

            "files":
            len(self.scan()),

            "time":
            str(datetime.now())

        }



if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Loader Engine V1.0"
    )

    print("="*50)


    engine=LoaderEngine()


    print(
        json.dumps(
            engine.report(),
            indent=4,
            ensure_ascii=False
        )
    )