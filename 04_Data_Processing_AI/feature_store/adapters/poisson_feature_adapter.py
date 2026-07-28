
# -*- coding: utf-8 -*-



class PoissonFeatureAdapter:



    def get_poisson_features(
        self,
        data
    ):


        return {


        "lambda_home":
        data.get(
            "lambda_home",
            0
        ),


        "lambda_away":
        data.get(
            "lambda_away",
            0
        )


        }

