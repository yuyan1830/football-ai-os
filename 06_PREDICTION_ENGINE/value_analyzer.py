
# -*- coding: utf-8 -*-



class ValueAnalyzer:



    def calculate(
        self,
        model_probability,
        market_probability
    ):



        value={}



        for key in model_probability:


            value[key]=round(

                model_probability[key]

                -

                market_probability.get(

                    key,

                    0

                ),

                4

            )



        return value



