
# -*- coding: utf-8 -*-


class DataRouter:


    def route(self,model):


        routes={


            "Elo":
            [
                "team_strength",
                "league_strength"
            ],


            "Dixon-Coles":
            [
                "attack",
                "defense",
                "goal_pattern"
            ],


            "Poisson":
            [
                "goal_rate",
                "scoring_distribution"
            ],


            "XGBoost":
            [
                "all_features"
            ],


            "Fusion":
            [
                "model_outputs"
            ]

        }


        return routes.get(
            model,
            []
        )



if __name__=="__main__":

    print(
        DataRouter().route("Elo")
    )
