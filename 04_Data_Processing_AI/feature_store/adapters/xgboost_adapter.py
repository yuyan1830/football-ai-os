
class XGBoostAdapter:

    def transform(self, features):

        return {
            "model":"XGBoost",
            "features":[
                "all_features"
            ],
            "input":features
        }


if __name__=="__main__":
    print(XGBoostAdapter().transform({}))
