# -*- coding: utf-8 -*-

"""
Football AI OS
Data Manager V1.0
"""


from dataset_manager import DatasetManager



class DataManager:


    def __init__(self):

        self.dataset_manager = DatasetManager()



    def status(self):

        return {

            "module":
            "02_DATA_PLATFORM",

            "service":
            "data_manager",

            "datasets":
            len(
                self.dataset_manager.get_datasets()
            ),

            "status":
            "active"

        }



if __name__=="__main__":


    manager = DataManager()


    print(
        manager.status()
    )