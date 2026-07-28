
# -*- coding: utf-8 -*-

import json



class FeatureDatasetGenerator:


    def generate(
        self,
        data,
        output
    ):


        with open(
            output,
            "w",
            encoding="utf-8"
        ) as f:


            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )


        return True


