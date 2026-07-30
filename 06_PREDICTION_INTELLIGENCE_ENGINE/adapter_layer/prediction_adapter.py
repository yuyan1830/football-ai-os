# -*- coding: utf-8 -*-

"""
Football AI OS Ω+ V3.2.1

Prediction Adapter

连接 Model Connector
"""


import sys
import os


ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


sys.path.append(ROOT)


from advanced_model_connector.elo_connector import EloConnector
from advanced_model_connector.dixon_coles_connector import DixonColesConnector
from advanced_model_connector.poisson_connector import PoissonConnector
from advanced_model_connector.xgboost_connector import XGBoostConnector



class PredictionAdapter:



    def __init__(self):

        self.status="READY"



    def connect_models(self):


        return {


            "elo":

            EloConnector().connect(),


            "dixon_coles":

            DixonColesConnector().connect(),


            "poisson":

            PoissonConnector().connect(),


            "xgboost":

            XGBoostConnector().connect()


        }




    def predict(self,match):


        models = self.connect_models()



        return {


            "match":

            match,


            "models":

            models,


            "status":

            "REAL_CONNECTOR_READY"


        }




    def health(self):


        return {


            "module":

            "PredictionAdapter",


            "status":

            self.status


        }



if __name__=="__main__":


    adapter=PredictionAdapter()


    print(

        adapter.predict(

            {

            "home":"Manchester City",

            "away":"Liverpool"

            }

        )

    )

