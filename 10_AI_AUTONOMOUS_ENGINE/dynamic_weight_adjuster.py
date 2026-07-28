

# -*- coding:utf-8 -*-



class DynamicWeightAdjuster:



    def calculate(

        self,

        weights,

        performance

    ):



        result={}



        for model,value in weights.items():


            factor=performance.get(

                model,

                1

            )


            result[model]=round(

                value*factor,

                3

            )



        return result



