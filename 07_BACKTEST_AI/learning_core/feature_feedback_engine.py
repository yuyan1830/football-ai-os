# -*- coding: utf-8 -*-


class FeatureFeedbackEngine:


    def __init__(self):

        self.version="V1.0"



    def analyze(
        self,
        feature_errors
    ):


        result=[]


        for item in feature_errors:


            result.append({

                "feature":
                    item.get(
                        "feature"
                    ),

                "impact":
                    "REVIEW",

                "recommendation":
                    "CHECK_WEIGHT"

            })


        return {


            "feature_review":
                True,


            "count":
                len(result),


            "items":
                result,


            "version":
                self.version

        }
