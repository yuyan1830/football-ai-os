
# -*- coding: utf-8 -*-



import json



class ModelTrainingExporter:



    def export(
        self,
        dataset,
        path
    ):


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:


            json.dump(
                dataset,
                f,
                indent=4,
                ensure_ascii=False
            )


