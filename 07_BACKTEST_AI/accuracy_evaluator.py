
# -*- coding: utf-8 -*-



class AccuracyEvaluator:



    def calculate(
        self,
        predictions,
        results
    ):


        total=len(

            predictions

        )


        correct=0



        for prediction,result in zip(

            predictions,

            results

        ):


            if prediction == result:


                correct +=1



        accuracy=0



        if total>0:


            accuracy=correct/total



        return {


            "total":

            total,


            "correct":

            correct,


            "accuracy":

            round(

                accuracy,

                4

            )


        }



