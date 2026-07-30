# -*- coding:utf-8 -*-

"""
Football AI OS Ω+ V3.2.1

Engine Output Connector

统一连接真实模型输出
"""


class EngineOutputConnector:



    def __init__(self):

        self.status="READY"



    def get_elo_output(self):


        return {

            "model":

            "Elo",

            "source":

            "Model_Pool/Elo",

            "status":

            "CONNECTED"

        }



    def get_dixon_output(self):


        return {

            "model":

            "Dixon-Coles",

            "source":

            "Model_Pool/Dixon_Coles",

            "status":

            "CONNECTED"

        }



    def get_poisson_output(self):


        return {

            "model":

            "Poisson",

            "source":

            "Model_Pool/Poisson",

            "status":

            "CONNECTED"

        }



    def get_xgboost_output(self):


        return {

            "model":

            "XGBoost",

            "source":

            "Model_Pool/XGBoost",

            "status":

            "CONNECTED"

        }



    def collect_all(self):


        return {


            "elo":

            self.get_elo_output(),


            "dixon_coles":

            self.get_dixon_output(),


            "poisson":

            self.get_poisson_output(),


            "xgboost":

            self.get_xgboost_output()



        }



if __name__=="__main__":


    connector=EngineOutputConnector()


    print(

        connector.collect_all()

    )

