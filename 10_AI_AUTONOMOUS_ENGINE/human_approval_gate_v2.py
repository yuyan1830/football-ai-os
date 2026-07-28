
# -*- coding:utf-8 -*-


class HumanApprovalGate:


    def check(self,status):

        if status == "PASS":

            return {

                "approval":

                "WAITING_HUMAN_APPROVAL"

            }


        return {

            "approval":

            "BLOCKED"

        }

