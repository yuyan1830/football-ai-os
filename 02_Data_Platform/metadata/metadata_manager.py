# -*- coding: utf-8 -*-

"""
Football AI OS
Metadata Manager
V1.0
"""


import json
import os


class MetadataManager:


    def __init__(self):

        self.file = os.path.join(

            os.path.dirname(__file__),

            "metadata_registry.json"

        )


    def load(self):

        with open(

            self.file,

            "r",

            encoding="utf-8"

        ) as f:

            return json.load(f)



    def list_datasets(self):

        data = self.load()

        return data["datasets"]



    def status(self):

        return {

            "module":
            "02_DATA_PLATFORM",

            "service":
            "metadata_manager",

            "datasets":
            len(self.list_datasets()),

            "status":
            "active"

        }



if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Metadata Manager V1.0"
    )

    print("="*50)


    manager = MetadataManager()


    print(

        manager.status()

    )