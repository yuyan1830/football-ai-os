
# -*- coding: utf-8 -*-

import math



class GoalDistribution:



    def poisson(
        self,
        expected_goal,
        goal
    ):


        return (

            math.pow(

                expected_goal,

                goal

            )

            *

            math.exp(

                -expected_goal

            )

            /

            math.factorial(

                goal

            )

        )



    def generate(
        self,
        home_xg,
        away_xg,
        max_goal=5
    ):


        result={}



        for home in range(max_goal+1):


            for away in range(max_goal+1):


                probability=(


                    self.poisson(

                        home_xg,

                        home

                    )


                    *

                    self.poisson(

                        away_xg,

                        away

                    )

                )



                result[

                    f"{home}-{away}"

                ]=round(

                    probability,

                    6

                )



        return result



