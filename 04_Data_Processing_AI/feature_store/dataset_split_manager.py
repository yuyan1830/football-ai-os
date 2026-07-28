
# -*- coding: utf-8 -*-



class DatasetSplitManager:



    def split(
        self,
        dataset
    ):


        total=len(dataset)


        train_end=int(
            total*0.8
        )


        return {


        "train":

        dataset[:train_end],


        "validation":

        dataset[train_end:]


        }


