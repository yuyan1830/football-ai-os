
# -*- coding: utf-8 -*-



class PredictionService:



    def __init__(
        self,
        model
    ):

        self.model=model



    def predict(
        self,
        features
    ):


        result=self.model.predict(

            features

        )


        return result



    def status(self):


        return {


            "service":

            "READY"


        }



