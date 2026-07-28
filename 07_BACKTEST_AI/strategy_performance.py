
# -*- coding: utf-8 -*-



class StrategyPerformance:



    def evaluate(
        self,
        records
    ):



        return {


            "strategy":

            "Football AI Strategy",


            "samples":

            len(records),


            "status":

            "COMPLETED"


        }



    def compare(
        self,
        strategies
    ):


        return sorted(

            strategies,

            key=lambda x:x.get(

                "roi",

                0

            ),

            reverse=True

        )



