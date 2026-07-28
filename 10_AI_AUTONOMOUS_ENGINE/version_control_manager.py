

# -*- coding:utf-8 -*-



class VersionControlManager:



    def __init__(self):

        self.records=[]



    def save_version(

        self,

        version,

        change

    ):


        self.records.append(

            {


            "version":

            version,


            "change":

            change


            }

        )


        return True




    def history(self):


        return self.records



