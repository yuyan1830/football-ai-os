
# -*- coding: utf-8 -*-



class FeatureQueryEngine:


    def recent_matches(
        self,
        matches,
        limit=10
    ):


        return matches[-limit:]


