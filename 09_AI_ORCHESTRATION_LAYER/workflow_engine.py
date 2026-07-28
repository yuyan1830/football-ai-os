
# -*- coding: utf-8 -*-



class WorkflowEngine:



    def __init__(self):

        self.workflow=[]



    def add_step(

        self,

        step

    ):

        self.workflow.append(step)



    def run(self):


        result=[]


        for step in self.workflow:

            result.append(step)



        return {


            "workflow":

            result,


            "status":

            "COMPLETED"


        }



