
# -*- coding:utf-8 -*-

class ModelRegistry:


    def __init__(self):

        self.models={

            "Elo":"V1.0",

            "Dixon-Coles":"V1.0",

            "Poisson":"V1.0",

            "XGBoost":"V1.0",

            "Fusion":"V1.0"

        }


    def register(self,name,version):

        self.models[name]=version


    def list_models(self):

        return self.models



