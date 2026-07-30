# -*- coding: utf-8 -*-

"""
Football AI OS Ω+ V3.2.1

Prediction Adapter

统一预测模型调用入口
"""


class PredictionAdapter:


    def __init__(self):

        self.status = "READY"



    def predict(self, match):


        result = {


            "match": match,


            "models": {


                "elo": "READY",

                "dixon_coles": "READY",

                "poisson": "READY",

                "xgboost": "READY"


            },


            "status":

            "PREDICTION_ADAPTER_READY"


        }


        return result



    def health(self):


        return {


            "module":

            "PredictionAdapter",


            "status":

            self.status


        }



if __name__ == "__main__":


    adapter = PredictionAdapter()


    print(

        adapter.predict(

            {

            "home":"Manchester City",

            "away":"Liverpool"

            }

        )

    )

