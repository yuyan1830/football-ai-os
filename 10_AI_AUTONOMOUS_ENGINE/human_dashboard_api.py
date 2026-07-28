

# -*- coding:utf-8 -*-



class HumanDashboardAPI:



    def get_status(

        self,

        system

    ):


        return {


            "system":

            system,


            "human_control":

            True,


            "approval_required":

            True



        }




    def get_pending_tasks(

        self

    ):


        return {


            "tasks":

            []



        }



