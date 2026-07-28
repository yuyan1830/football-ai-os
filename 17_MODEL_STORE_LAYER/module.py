
# -*- coding: utf-8 -*-

BASE=r"E:\football_v"


class ModelStore:

    def load_models(self):

        return [

        "ELO",

        "DIXON_COLES",

        "POISSON",

        "XGBOOST",

        "V38.8.1",

        "MARKET_RISK_2.0"

        ]


if __name__=="__main__":

    print(ModelStore().load_models())

