
# -*- coding: utf-8 -*-


import os
import json



class FeatureMatchReader:


    def __init__(self, path):

        self.path = path



    def read_json(self):


        if not os.path.exists(
            self.path
        ):

            return []


        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:


            return json.load(f)


