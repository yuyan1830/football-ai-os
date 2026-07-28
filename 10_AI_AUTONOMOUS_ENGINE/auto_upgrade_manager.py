

# -*- coding:utf-8 -*-


class AutoUpgradeManager:



    def create_upgrade_candidate(

        self,

        model,

        changes

    ):


        return {


            "model":

            model,


            "changes":

            changes,


            "status":

            "CANDIDATE"



        }



    def submit_validation(

        self,

        candidate

    ):


        candidate["status"]="WAIT_VALIDATION"


        return candidate



    def release(

        self,

        candidate

    ):


        candidate["status"]="RELEASED"


        return candidate



