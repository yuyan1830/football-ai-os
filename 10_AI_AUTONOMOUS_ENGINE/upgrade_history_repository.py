

# -*- coding:utf-8 -*-



class UpgradeHistoryRepository:



    def __init__(self):


        self.records=[]




    def save(

        self,

        upgrade

    ):


        self.records.append(

            upgrade

        )


        return {


            "saved":

            True



        }




    def all(self):


        return self.records



