
# -*- coding: utf-8 -*-


class ModelInterface:


    models=[

        "Elo",

        "Dixon-Coles",

        "Poisson",

        "XGBoost",

        "Fusion"

    ]



    def available_models(self):

        return self.models



if __name__=="__main__":

    print(
        ModelInterface().available_models()
    )
