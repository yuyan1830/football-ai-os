
# -*- coding: utf-8 -*-



class BacktestEngine:



    def evaluate(
        self,
        prediction,
        result
    ):


        return {


            "prediction":

            prediction,


            "actual":

            result,


            "correct":

            prediction == result


        }



    def run(
        self,
        dataset
    ):


        return {


            "samples":

            len(dataset),


            "status":

            "COMPLETED"


        }



