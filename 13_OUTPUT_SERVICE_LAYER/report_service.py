# -*- coding: utf-8 -*-

"""
Football AI OS
Output Service V1.0
"""


class ReportService:


    def generate(self, prediction):


        return {


            "system":
                "Football AI OS",


            "match":
                prediction.get(
                    "match",
                    {}
                ),


            "analysis":
                {


                "model_result":
                    prediction.get(
                        "model_result",
                        {}
                    ),


                "decision":
                    prediction.get(
                        "decision",
                        {})

                },


            "runtime":
                prediction.get(
                    "runtime",
                    {}
                ),


            "status":
                "REPORT_READY"

        }

