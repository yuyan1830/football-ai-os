
class DixonColesAdapter:

    def transform(self, features):

        return {
            "model":"Dixon-Coles",
            "features":[
                "attack",
                "defense",
                "goal_pattern"
            ],
            "input":features
        }


if __name__=="__main__":
    print(DixonColesAdapter().transform({}))
