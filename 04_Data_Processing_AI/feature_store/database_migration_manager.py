
# -*- coding: utf-8 -*-



class DatabaseMigrationManager:



    current_version="V2.1"



    def get_version(self):

        return self.current_version



    def migrate(self):

        return {


            "migration":

            self.current_version,


            "status":

            "READY"


        }



