
# -*- coding: utf-8 -*-



class DataPromotionService:



    allowed_flow={


        "development":

        [

            "validation"

        ],


        "validation":

        [

            "production"

        ]


    }



    def can_promote(
        self,
        source,
        target
    ):


        return target in self.allowed_flow.get(

            source,

            []

        )


