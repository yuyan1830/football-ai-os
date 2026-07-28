
# -*- coding: utf-8 -*-



class TaskScheduler:



    def __init__(self):

        self.tasks=[]



    def register(

        self,

        task

    ):

        self.tasks.append(task)



    def schedule(self):


        return {


            "tasks":

            self.tasks,


            "status":

            "SCHEDULED"


        }



