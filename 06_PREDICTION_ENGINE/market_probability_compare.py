
# -*- coding: utf-8 -*-



class MarketProbabilityCompare:



    def compare(
        self,
        model,
        market
    ):


        result={}



        for key in model:


            result[key]={


                "model":

                model[key],


                "market":

                market.get(

                    key,

                    0

                ),


                "difference":

                round(

                    model[key]

                    -

                    market.get(

                        key,

                        0

                    ),

                    4

                )


            }



        return result



