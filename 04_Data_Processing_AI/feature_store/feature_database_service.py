
# -*- coding: utf-8 -*-

import os
import sqlite3



class FeatureDatabaseService:


    def __init__(self, database_path):

        self.database_path = database_path



    def check_database(self):

        return os.path.exists(
            self.database_path
        )



    def connect(self):

        if not self.check_database():

            return None


        return sqlite3.connect(
            self.database_path
        )


