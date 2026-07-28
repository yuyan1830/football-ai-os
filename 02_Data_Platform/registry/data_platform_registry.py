# -*- coding:utf-8 -*-

"""
Football AI OS
Data Platform Registry V1.0
"""


import json
import os



BASE=os.path.dirname(__file__)


FILE=os.path.join(
    BASE,
    "data_platform_registry.json"
)



class DataRegistry:


    def load(self):

        with open(
            FILE,
            "r",
            encoding="utf-8-sig"
        ) as f:

            return json.load(f)



    def save(self,data):


        with open(
            FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )



    def activate(self):


        data=self.load()


        data["status"]="active"


        self.save(data)


        return data



if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Data Platform Registry V1.0"
    )

    print("="*50)


    print(
        DataRegistry().activate()
    )