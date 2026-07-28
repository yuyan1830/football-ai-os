# -*- coding: utf-8 -*-

"""
Football AI OS
Data Lineage Engine
V1.0
"""


import json
import os
from datetime import datetime



class DataLineage:


    def __init__(self):

        self.registry = os.path.join(

            os.path.dirname(__file__),

            "lineage_registry.json"

        )


        if not os.path.exists(self.registry):

            self.create()



    def create(self):

        data = {

            "framework":
            "Football AI OS",

            "module":
            "02_DATA_PLATFORM",

            "version":
            "V1.0",

            "lineage":

            []

        }


        with open(

            self.registry,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                data,

                f,

                indent=4,

                ensure_ascii=False

            )



    def load(self):

        with open(

            self.registry,

            "r",

            encoding="utf-8"

        ) as f:

            return json.load(f)



    def register(

        self,

        source,

        target,

        process

    ):


        data = self.load()


        record = {


            "source":
            source,


            "target":
            target,


            "process":
            process,


            "time":
            str(datetime.now())

        }


        data["lineage"].append(record)



        with open(

            self.registry,

            "w",

            encoding="utf-8"

        ) as f:


            json.dump(

                data,

                f,

                indent=4,

                ensure_ascii=False

            )



    def status(self):

        data=self.load()


        return {

            "module":
            "02_DATA_PLATFORM",


            "service":
            "data_lineage",


            "records":
            len(data["lineage"]),


            "status":
            "active"

        }



if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Data Lineage V1.0"
    )

    print("="*50)



    engine=DataLineage()


    engine.register(

        "01_DATA_SOURCE",

        "02_DATA_PLATFORM/raw",

        "import"

    )


    print(

        engine.status()

    )