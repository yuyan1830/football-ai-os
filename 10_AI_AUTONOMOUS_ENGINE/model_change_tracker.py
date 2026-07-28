

# -*- coding:utf-8 -*-



class ModelChangeTracker:



    def __init__(self):


        self.changes=[]



    def record(

        self,

        model,

        old_version,

        new_version,

        reason

    ):


        item={


            "model":

            model,


            "old_version":

            old_version,


            "new_version":

            new_version,


            "reason":

            reason



        }


        self.changes.append(item)


        return item




    def history(self):


        return self.changes



