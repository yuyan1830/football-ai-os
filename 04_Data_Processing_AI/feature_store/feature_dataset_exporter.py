
# -*- coding: utf-8 -*-

import json


class FeatureDatasetExporter:


    def export(
        self,
        data,
        path
    ):


        with open(
            path,
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


