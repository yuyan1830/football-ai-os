
# -*- coding: utf-8 -*-



class TrainingDatasetBuilder:



    def build(
        self,
        feature_dataset
    ):


        dataset=[]



        for row in feature_dataset:


            dataset.append({

                "features":

                row,


                "label":

                row.get(
                    "result"
                )

            })


        return dataset


