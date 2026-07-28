
# -*- coding: utf-8 -*-


class OptimizationSuggestionEngine:



    def generate(

        self,

        error_report

    ):


        suggestion={


            "require_human":

            True,


            "risk":

            "MEDIUM",


            "status":

            "WAITING_APPROVAL"



        }



        rate = error_report.get(

            "error_rate",

            0

        )



        if rate >= 0.30:


            suggestion["action"] = (

                "Generate optimization proposal"

            )


        else:


            suggestion["action"] = (

                "Continue monitoring"

            )



        return suggestion



