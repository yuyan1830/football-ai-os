
# -*- coding:utf-8 -*-


import datetime



class DecisionLogger:



    def log(

        self,

        model,

        error_rate,

        decision

    ):


        return {


            "time":

            str(datetime.datetime.now()),


            "model":

            model,


            "error_rate":

            error_rate,


            "decision":

            decision,


            "operator":

            "human"



        }



