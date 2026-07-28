# -*- coding:utf-8 -*-

"""
Football AI OS
Raw Data Registry V1.0
"""


import json
import os



BASE_DIR=os.path.dirname(__file__)


REGISTRY=os.path.join(
    BASE_DIR,
    "raw_registry.json"
)



class RawRegistry:


    def load(self):

        with open(
            REGISTRY,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



    def register(self,files):


        data=self.load()


        data["files"]=files


        with open(
            REGISTRY,
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


    registry=RawRegistry()


    print(
        registry.load()
    )