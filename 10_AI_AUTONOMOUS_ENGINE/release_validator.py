

# -*- coding:utf-8 -*-



class ReleaseValidator:



    def validate(

        self,

        backtest_result

    ):



        if (

            backtest_result.get(

                "accuracy",

                0

            )

            >

            backtest_result.get(

                "previous_accuracy",

                0

            )

        ):


            return {


                "release":

                True,


                "status":

                "APPROVED"



            }




        return {


            "release":

            False,


            "status":

            "REJECTED"



        }



