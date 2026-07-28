
# -*- coding: utf-8 -*-

import os
import sqlite3


class FeatureDatabaseReader:


    def __init__(self, database_path):

        self.database_path = database_path



    def connect(self):

        if not os.path.exists(
            self.database_path
        ):

            return None


        return sqlite3.connect(
            self.database_path
        )


