
# -*- coding: utf-8 -*-



class ProbabilityEvaluator:



    def evaluate(
        self,
        probabilities,
        outcomes
    ):


        result={


            "samples":

            len(probabilities),


            "status":

            "EVALUATED"


        }



        return result



    def calibration_score(
        self,
        predicted,
        actual
    ):


        error=abs(

            predicted-actual

        )



        return {


            "calibration_error":

            round(

                error,

                4

            )


        }



