
# -*- coding: utf-8 -*-


class TimeWindowAnalyzer:


    WINDOWS=[

        7,

        30,

        90,

        180

    ]



    def analyze(

        self,

        history

    ):


        result={}


        for window in self.WINDOWS:


            result[str(window)+"_days"]={


                "samples":

                len(history[-window:]),


                "data":

                history[-window:]

            }


        return result

