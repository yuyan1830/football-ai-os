# -*- coding:utf-8 -*-

"""
Football AI OS

AI Model Controller

Version V1.0

"""


import json

from datetime import datetime



class ModelController:


    def status(self):

        return {


            "framework":

            "Football AI OS",


            "module":

            "05_AI_INTELLIGENCE_LAYER",


            "service":

            "model_controller",


            "version":

            "V1.0",


            "status":

            "active",


            "models":

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



if __name__=="__main__":


    print("="*50)

    print(
    "Football AI OS AI Model Controller V1.0"
    )

    print("="*50)



    print(

        json.dumps(

            ModelController().status(),

            indent=4,

            ensure_ascii=False

        )

    )



