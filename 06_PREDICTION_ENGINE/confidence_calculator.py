
# -*- coding: utf-8 -*-



class ConfidenceCalculator:



    def calculate(
        self,
        probability
    ):


        max_probability=max(

            probability.values()

        )



        if max_probability >= 0.85:


            level="A"



        elif max_probability >=0.70:


            level="B"



        else:


            level="C"



        return {


            "confidence":

            level,


            "score":

            round(

                max_probability*100,

                2

            )


        }



