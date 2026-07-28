import json
import os


class FeatureSchema:

    def __init__(self):
        self.path=os.path.join(
            os.path.dirname(__file__),
            "schema",
            "feature_schema.json"
        )

    def load(self):
        with open(
            self.path,
            "r",
            encoding="utf-8-sig"
        ) as f:
            return json.load(f)


if __name__=="__main__":
    print(FeatureSchema().load())
