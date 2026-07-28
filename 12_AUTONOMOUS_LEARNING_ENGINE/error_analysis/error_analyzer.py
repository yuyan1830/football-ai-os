
# -*- coding:utf-8 -*-


class ErrorAnalyzer:


    def analyze(self,prediction,actual):

        return {

            "prediction":
            prediction,

            "actual":
            actual,

            "error":
            abs(prediction-actual)

        }

