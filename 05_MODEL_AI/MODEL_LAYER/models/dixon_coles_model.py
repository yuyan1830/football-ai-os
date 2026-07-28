
# -*- coding: utf-8 -*-



class DixonColesModel:



    def __init__(self):

        self.name="Dixon-Coles"



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

            0.35,


            "draw":

            0.32,


            "away_win":

            0.33


        }



