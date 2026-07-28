
# -*- coding: utf-8 -*-

BASE=r"E:\football_v"


class ExecutionEngine:


    def predict(self):

        return {

        "status":
        "READY",

        "pipeline":
        [

        "ELO",

        "DIXON_COLES",

        "POISSON",

        "XGBOOST",

        "HANDICAP",

        "MARKET_RISK",

        "KELLY"

        ]

        }


if __name__=="__main__":

    print(
    ExecutionEngine().predict()
    )

