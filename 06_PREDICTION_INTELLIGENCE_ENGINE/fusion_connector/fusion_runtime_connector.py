# -*- coding:utf-8 -*-

"""
Football AI OS Ω+ V3.2.1

Fusion Runtime Connector

连接 Probability Layer 与 Fusion Engine
"""


class FusionRuntimeConnector:


    def __init__(self):

        self.status="READY"



    def prepare_input(
        self,
        probabilities
    ):


        return {


            "elo":

            probabilities.get(
                "elo",
                {}
            ),


            "dixon_coles":

            probabilities.get(
                "dixon_coles",
                {}
            ),


            "poisson":

            probabilities.get(
                "poisson",
                {}
            ),


            "xgboost":

            probabilities.get(
                "xgboost",
                {}
            )


        }



    def fusion_input_check(
        self,
        data
    ):


        required=[

            "elo",

            "dixon_coles",

            "poisson",

            "xgboost"

        ]


        return all(

            x in data

            for x in required

        )



if __name__=="__main__":


    connector=FusionRuntimeConnector()


    print(

        connector.fusion_input_check(

            {

            "elo":{},


            "dixon_coles":{},


            "poisson":{},


            "xgboost":{}

            }

        )

    )

