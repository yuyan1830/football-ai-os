
# -*- coding: utf-8 -*-



class ValidationDatasetChecker:



    required_fields=[


        "home_team",

        "away_team",

        "result"


    ]



    def check(
        self,
        dataset
    ):


        for row in dataset:


            for field in self.required_fields:


                if field not in row:

                    return False



        return True


