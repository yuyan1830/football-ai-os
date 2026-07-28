

# -*- coding:utf-8 -*-



class WeeklyEvolutionAnalyzer:



    def analyze(

        self,

        records

    ):



        total=len(records)



        return {


            "period":

            "weekly",


            "records":

            total,


            "error_rate":

            self.calculate_error(records)



        }




    def calculate_error(

        self,

        records

    ):



        if len(records)==0:


            return 0



        errors=0



        for item in records:


            if item.get(

                "error",

                False

            ):


                errors+=1



        return round(

            errors/len(records),

            3

        )



