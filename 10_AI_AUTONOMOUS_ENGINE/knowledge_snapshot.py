

# -*- coding:utf-8 -*-



import datetime



class KnowledgeSnapshot:



    def create(

        self,

        data

    ):


        return {


            "time":

            str(datetime.datetime.now()),


            "snapshot":

            data



        }



