
# -*- coding: utf-8 -*-

import sqlite3
import os


class DatabaseConnector:


    def __init__(self, db_path):

        self.db_path=db_path



    def connect(self):

        if not os.path.exists(self.db_path):

            return None


        return sqlite3.connect(
            self.db_path
        )


