
# -*- coding: utf-8 -*-



class PredictionRegistry:



    def __init__(self):

        self.registry={}



    def register(
        self,
        name,
        service
    ):


        self.registry[name]=service



    def get(
        self,
        name
    ):


        return self.registry.get(

            name

        )



    def list(self):


        return list(

            self.registry.keys()

        )



