

# -*- coding:utf-8 -*-



class UpgradePolicyManager:



    def check_policy(

        self,

        approval,

        backtest

    ):



        if (

            approval=="APPROVED"

            and

            backtest=="PASS"

        ):


            return {


                "allow_release":

                True



            }



        return {


            "allow_release":

            False



        }



