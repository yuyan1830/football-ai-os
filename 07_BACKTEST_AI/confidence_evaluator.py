
# -*- coding: utf-8 -*-



class ConfidenceEvaluator:



    def evaluate(
        self,
        confidence_levels,
        results
    ):


        report={}



        for level in set(

            confidence_levels

        ):


            report[level]={


                "count":

                confidence_levels.count(

                    level

                )


            }



        return report



    def score(
        self,
        confidence,
        correct
    ):


        if confidence=="A":


            weight=1.0


        elif confidence=="B":


            weight=0.8


        else:


            weight=0.6



        if correct:


            return weight



        return 0



