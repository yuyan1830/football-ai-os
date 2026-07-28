

# -*- coding:utf-8 -*-



class ParameterEffectAnalyzer:



    def analyze(

        self,

        before,

        after

    ):



        result={


            "accuracy_change":

            after.get(

                "accuracy",

                0

            )

            -

            before.get(

                "accuracy",

                0

            ),



            "roi_change":

            after.get(

                "roi",

                0

            )

            -

            before.get(

                "roi",

                0



            )



        }



        return result



