
# -*- coding: utf-8 -*-



class ProbabilityCalculator:



    def normalize(
        self,
        probability
    ):


        total=sum(

            probability.values()

        )


        return {


            key:

            value/total


            for key,value

            in probability.items()


        }



