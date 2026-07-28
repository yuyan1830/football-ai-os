
# -*- coding: utf-8 -*-



class ProbabilityCalibrator:



    def calibrate(
        self,
        probability
    ):



        total=sum(

            probability.values()

        )



        if total==0:


            return probability



        return {


            key:

            round(

                value/total,

                4

            )


            for key,value

            in probability.items()


        }



