
# -*- coding: utf-8 -*-



class ModelSelfOptimizer:



    MODELS=[


        "ELO",

        "Dixon-Coles",

        "Poisson",

        "XGBoost",

        "Fusion"


    ]




    def analyze(

        self,

        errors

    ):



        result={}



        for model in self.MODELS:


            result[model]={


                "error_contribution":

                0,


                "suggestion":

                "observe"


            }



        return result



