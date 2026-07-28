
class EloAdapter:

    def transform(self, features):

        return {
            "model":"Elo",
            "features":[
                "team_strength",
                "league_strength"
            ],
            "input":features
        }


if __name__=="__main__":
    print(EloAdapter().transform({}))
