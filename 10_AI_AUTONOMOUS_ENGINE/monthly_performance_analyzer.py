

# -*- coding:utf-8 -*-



class MonthlyPerformanceAnalyzer:



    def analyze(

        self,

        performance

    ):



        return {


            "period":

            "monthly",


            "accuracy":

            performance.get(

                "accuracy",

                0

            ),


            "roi":

            performance.get(

                "roi",

                0

            ),


            "stability":

            performance.get(

                "stability",

                0

            )



        }



