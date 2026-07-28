
# -*- coding:utf-8 -*-


class ApprovalWorkflow:



    STATUS=[


        "PENDING",

        "APPROVED",

        "REJECTED",

        "OBSERVE",

        "ROLLBACK"


    ]



    def update(

        self,

        status

    ):


        if status in self.STATUS:


            return {


                "current_status":

                status


            }


        return {


            "current_status":

            "INVALID"


        }



