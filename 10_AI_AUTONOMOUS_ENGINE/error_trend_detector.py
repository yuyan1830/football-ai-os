
# -*- coding: utf-8 -*-


class ErrorTrendDetector:



    def detect(

        self,

        rates

    ):


        trend="NORMAL"



        if rates.get(

            "7_days",

            0

        ) > rates.get(

            "30_days",

            0

        ):


            trend="RISING"



        return {


            "trend":

            trend


        }

