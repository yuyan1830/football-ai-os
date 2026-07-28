
# -*- coding:utf-8 -*-


class Evaluator:


    def evaluate(self,prediction,result):

        return {

            "error":

            abs(prediction-result)

        }

