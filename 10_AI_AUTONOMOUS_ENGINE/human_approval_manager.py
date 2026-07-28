
# -*- coding:utf-8 -*-


class HumanApprovalManager:



    def create_request(self, report):


        return {


            "status":

            "PENDING",


            "require_human":

            True,


            "report":

            report



        }



    def approve(self):


        return {

            "decision":

            "APPROVED"

        }



    def reject(self):


        return {

            "decision":

            "REJECTED"

        }



