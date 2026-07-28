
# -*- coding: utf-8 -*-


class ErrorRateCalculator:


    def calculate(
        self,
        total,
        errors
    ):

        if total == 0:

            return 0


        return round(

            errors / total,

            4

        )

