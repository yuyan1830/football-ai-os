

# -*- coding:utf-8 -*-



class OptimizationHistory:



    def __init__(self):


        self.history=[]



    def add_record(

        self,

        model,

        error_before,

        error_after,

        decision

    ):


        record={


            "model":

            model,


            "error_before":

            error_before,


            "error_after":

            error_after,


            "decision":

            decision



        }


        self.history.append(record)


        return record



    def get_history(self):


        return self.history



