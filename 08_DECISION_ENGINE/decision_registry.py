
# -*- coding: utf-8 -*-



class DecisionRegistry:



    def __init__(self):


        self.registry={}




    def register(

        self,

        name,

        engine

    ):


        self.registry[name]=engine




    def get(

        self,

        name

    ):


        return self.registry.get(name)




    def list(self):


        return list(

            self.registry.keys()

        )



