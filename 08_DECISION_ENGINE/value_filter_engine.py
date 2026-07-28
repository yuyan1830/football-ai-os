
# -*- coding: utf-8 -*-



class ValueFilterEngine:



    def calculate_value(

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




    def check_value(

        self,

        value

    ):



        max_value=max(

            value.values()

        )



        if max_value >=0.08:


            return "VALUE_FOUND"



        return "NO_VALUE"



