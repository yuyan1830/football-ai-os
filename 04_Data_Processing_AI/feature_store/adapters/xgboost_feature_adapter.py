
# -*- coding: utf-8 -*-



class XGBoostFeatureAdapter:



    def get_xgb_features(
        self,
        data
    ):


        return {


        "feature_vector":
        data.get(
            "feature_vector",
            []
        )


        }

