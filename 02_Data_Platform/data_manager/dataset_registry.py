# -*- coding: utf-8 -*-

"""
Football AI OS
Dataset Registry V1.0
"""

import os
import json
from datetime import datetime


BASE = os.path.dirname(__file__)

REGISTRY_FILE = os.path.join(
    BASE,
    "dataset_registry.json"
)


class DatasetRegistry:


    def __init__(self):

        self.file = REGISTRY_FILE



    def create(self):

        registry = {

            "framework":
            "Football AI OS",

            "module":
            "02_DATA_PLATFORM",

            "service":
            "dataset_registry",

            "version":
            "V1.0",

            "datasets":[

                {
                    "name":
                    "match_raw",

                    "type":
                    "football_match",

                    "status":
                    "ready"
                },


                {
                    "name":
                    "team_raw",

                    "type":
                    "football_team",

                    "status":
                    "ready"
                },


                {
                    "name":
                    "odds_raw",

                    "type":
                    "market_odds",

                    "status":
                    "planned"
                }

            ],


            "created":
            str(datetime.now())

        }


        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                registry,
                f,
                indent=4,
                ensure_ascii=False
            )


        return registry



    def load(self):

        if not os.path.exists(
            self.file
        ):

            return self.create()


        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Dataset Registry V1.0"
    )

    print("="*50)


    registry = DatasetRegistry()


    print(
        json.dumps(
            registry.create(),
            indent=4,
            ensure_ascii=False
        )
    )