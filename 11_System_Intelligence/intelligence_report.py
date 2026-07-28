
import json
import os


class IntelligenceReport:


    def generate(self,data,path):

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )


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
