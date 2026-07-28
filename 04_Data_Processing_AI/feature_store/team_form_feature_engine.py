
# -*- coding: utf-8 -*-



class TeamFormFeatureEngine:



    def calculate(
        self,
        history
    ):


        return {


        "last_5_form":

        history[-5:],


        "last_10_form":

        history[-10:]


        }


