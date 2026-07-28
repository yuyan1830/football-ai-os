

# -*- coding:utf-8 -*-



class RollbackManager:



    def __init__(self):


        self.current_version=None


        self.previous_version=None




    def save_version(

        self,

        version

    ):


        self.previous_version=self.current_version


        self.current_version=version



        return {


            "saved":

            version



        }




    def rollback(self):


        self.current_version=self.previous_version


        return {


            "status":

            "ROLLBACK_COMPLETE",


            "version":

            self.current_version



        }



