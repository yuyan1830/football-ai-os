# -*- coding:utf-8 -*-

"""
Market Decision Connector
"""


class MarketDecisionConnector:



    def combine(
        self,
        market,
        sentiment,
        handicap
    ):


        return {


            "market":

            market,


            "sentiment":

            sentiment,


            "handicap":

            handicap,


            "status":

            "MARKET_DECISION_READY"


        }

