
# -*- coding: utf-8 -*-



class DixonColesFeatureAdapter:



    def get_dixon_coles_features(
        self,
        data
    ):


        return {


        "attack_strength":
        data.get(
            "attack_strength",
            0
        ),


        "defence_strength":
        data.get(
            "defence_strength",
            0
        )


        }

