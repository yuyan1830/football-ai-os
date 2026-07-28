
# -*- coding: utf-8 -*-


class FusionExplainer:


    def explain(self,weights):

        return {

            "method":
            "weighted_probability_fusion",

            "weights":
            weights,

            "explanation":
            "model contribution analysis ready"

        }

