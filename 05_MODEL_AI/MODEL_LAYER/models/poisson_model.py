
# -*- coding: utf-8 -*-



class PoissonModel:



    def __init__(self):

        self.name="Poisson"



    def train(
        self,
        data
    ):


        return {


            "model":

            self.name,


            "status":

            "TRAINED"


        }



    def predict(
        self,
        features
    ):


        return {


            "home_win":

            0.38,


            "draw":

            0.29,


            "away_win":

            0.33


        }



