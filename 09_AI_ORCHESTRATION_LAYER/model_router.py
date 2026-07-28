
# -*- coding: utf-8 -*-



class ModelRouter:



    def __init__(self):


        self.models={


            "elo":

            "Elo Model",


            "dixon_coles":

            "Dixon-Coles Model",


            "poisson":

            "Poisson Model",


            "xgboost":

            "XGBoost Model",


            "fusion":

            "Fusion Model"


        }




    def register_model(

        self,

        name,

        model

    ):


        self.models[name]=model




    def route(

        self,

        task_type

    ):



        if task_type=="fast":


            return [


                "elo",


                "poisson"


            ]




        elif task_type=="deep":


            return [


                "elo",


                "dixon_coles",


                "poisson",


                "xgboost",


                "fusion"


            ]




        return [


            "fusion"


        ]





    def list_models(self):


        return self.models



