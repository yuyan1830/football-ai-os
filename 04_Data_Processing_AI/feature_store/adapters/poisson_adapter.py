
class PoissonAdapter:

    def transform(self, features):

        return {
            "model":"Poisson",
            "features":[
                "goal_rate",
                "attack_rate",
                "defense_rate"
            ],
            "input":features
        }


if __name__=="__main__":
    print(PoissonAdapter().transform({}))
