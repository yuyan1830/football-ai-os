
# -*- coding: utf-8 -*-



class RiskEngine:



    def analyze(
        self,
        probability,
        confidence
    ):


        max_probability=max(

            probability.values()

        )



        if max_probability >=0.80 and confidence=="A":


            risk="LOW"



        elif max_probability>=0.65:


            risk="MEDIUM"



        else:


            risk="HIGH"



        return {


            "risk_level":

            risk



        }



