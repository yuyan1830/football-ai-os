
# -*- coding: utf-8 -*-

import json


def load_models():

    models=[

        "Elo",

        "Dixon-Coles",

        "Poisson",

        "XGBoost",

        "V38.8.1 Handicap Model",

        "Market Risk Model 2.0"

    ]

    print({

        "module":
        "Model Loader",

        "loaded":
        models

    })


if __name__=="__main__":

    load_models()

