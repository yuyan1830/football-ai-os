
# -*- coding: utf-8 -*-



class EloFeatureAdapter:



    def get_elo_features(
        self,
        data
    ):


        return {


            "elo_home":
            data.get(
                "elo_home",
                0
            ),


            "elo_away":
            data.get(
                "elo_away",
                0
            )

        }

