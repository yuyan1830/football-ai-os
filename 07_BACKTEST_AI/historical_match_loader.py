
# -*- coding: utf-8 -*-



class HistoricalMatchLoader:



    def load(
        self,
        source
    ):


        return {


            "source":

            source,


            "status":

            "LOADED"


        }



    def count(
        self,
        matches
    ):


        return len(matches)



