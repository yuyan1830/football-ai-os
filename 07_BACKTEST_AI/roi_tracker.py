
# -*- coding: utf-8 -*-



class ROITracker:



    def __init__(self):

        self.records=[]



    def add_record(
        self,
        match_id,
        stake,
        profit
    ):


        self.records.append(


            {


                "match_id":

                match_id,


                "stake":

                stake,


                "profit":

                profit



            }


        )



    def calculate(self):


        total_stake=sum(


            item["stake"]

            for item

            in self.records


        )



        total_profit=sum(


            item["profit"]

            for item

            in self.records


        )



        roi=0



        if total_stake>0:


            roi=total_profit/total_stake



        return {


            "total_stake":

            total_stake,


            "total_profit":

            total_profit,


            "roi":

            round(

                roi,

                4

            )


        }



