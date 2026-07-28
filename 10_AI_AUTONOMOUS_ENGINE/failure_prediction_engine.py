

# -*- coding:utf-8 -*-


class FailurePredictionEngine:



    def predict(self,data):


        if data.get(

            "risk",

            0

        )>0.7:


            return "HIGH"



        return "LOW"



