
# -*- coding: utf-8 -*-



class DatasetSchemaValidator:



    required_fields=[

        "home_team",

        "away_team",

        "home_score",

        "away_score"

    ]



    def validate(
        self,
        data
    ):


        for row in data:


            for field in self.required_fields:


                if field not in row:

                    return False


        return True


