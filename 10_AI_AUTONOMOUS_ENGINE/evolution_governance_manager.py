

# -*- coding:utf-8 -*-


class EvolutionGovernanceManager:



    def __init__(self):

        self.status="READY"



    def submit_upgrade(self,request):


        return {


            "upgrade_request":

            request,


            "status":

            "PENDING_APPROVAL"


        }




    def approve(self):


        self.status="APPROVED"


        return self.status




