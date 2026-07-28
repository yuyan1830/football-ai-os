
class FusionAdapter:

    def transform(self, model_outputs):

        return {
            "model":"Fusion",
            "models":[
                "Elo",
                "Dixon-Coles",
                "Poisson",
                "XGBoost"
            ],
            "input":model_outputs
        }


if __name__=="__main__":
    print(FusionAdapter().transform({}))
