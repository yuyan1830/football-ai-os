
# -*- coding: utf-8 -*-


import json



class FeatureDatasetReporter:



    def report(
        self,
        data,
        path
    ):


        result={

            "dataset_size":
            len(data),

            "status":
            "READY"

        }


        with open(

            path,

            "w",

            encoding="utf-8"

        ) as f:


            json.dump(

                result,

                f,

                indent=4

            )


