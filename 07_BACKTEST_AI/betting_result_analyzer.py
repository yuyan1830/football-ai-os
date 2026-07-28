
# -*- coding: utf-8 -*-



class BettingResultAnalyzer:



    def analyze(
        self,
        bets
    ):


        wins=0

        losses=0



        for bet in bets:


            if bet.get(

                "result"

            )=="WIN":


                wins +=1



            else:


                losses +=1



        return {


            "wins":

            wins,


            "losses":

            losses,


            "total":

            len(bets)



        }



    def win_rate(
        self,
        bets
    ):


        if len(bets)==0:


            return 0



        wins=len(


            [

            x for x in bets

            if x.get("result")=="WIN"

            ]

        )



        return round(

            wins/len(bets),

            4

        )



