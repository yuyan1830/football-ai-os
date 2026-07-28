# -*- coding: utf-8 -*-

"""
Football AI OS
Dataset Manager V1.0
"""


from dataset_registry import DatasetRegistry



class DatasetManager:


    def __init__(self):

        self.registry = DatasetRegistry()



    def get_datasets(self):

        data = self.registry.load()

        return data.get(
            "datasets",
            []
        )



if __name__=="__main__":


    manager = DatasetManager()


    print(
        manager.get_datasets()
    )