
# -*- coding: utf-8 -*-



class PipelineController:



    def __init__(self):


        self.pipeline=[]




    def add_module(

        self,

        module

    ):


        self.pipeline.append(module)




    def execute(

        self,

        data

    ):



        result=data



        for module in self.pipeline:


            result=module(result)



        return result




    def info(self):


        return {


            "pipeline":

            self.pipeline,


            "status":

            "READY"


        }



