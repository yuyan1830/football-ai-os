# -*- coding:utf-8 -*-

"""
Football AI OS Ω+

Market Adapter

连接市场智能层
"""


class MarketAdapter:


    def __init__(self):

        self.status="READY"



    def collect(self,match):


        return {


            "match":match,


            "odds":

            "READY",


            "market_flow":

            "READY",


            "status":

            "MARKET_CONNECTED"


        }



if __name__=="__main__":


    print(

        MarketAdapter().collect(

            {

            "home":"A",

            "away":"B"

            }

        )

    )

