
# -*- coding: utf-8 -*-



class XGBoostModel:



    def __init__(self):

        self.name="XGBoost"



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

            0.42,


            "draw":

            0.28,


            "away_win":

            0.30


        }



