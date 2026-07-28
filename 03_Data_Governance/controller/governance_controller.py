# -*- coding:utf-8 -*-

"""
Football AI OS

Governance Controller

Version V1.0
"""


import os
import json
from datetime import datetime



class GovernanceController:



    def __init__(self):

        self.modules=[]



    def check_module(self,name,path):


        status=os.path.exists(path)


        self.modules.append(

            {

                "module":name,

                "path":path,

                "status":status

            }

        )




    def generate_status(self):


        total=len(self.modules)


        passed=sum(

            1 for x in self.modules

            if x["status"]

        )


        score=int(

            passed/total*100

        )



        return {


            "framework":

            "Football AI OS",


            "module":

            "03_DATA_GOVERNANCE",


            "service":

            "governance_controller",


            "version":

            "V1.0",


            "score":

            score,


            "status":

            "PASS" if score==100 else "WARNING",


            "components":

            self.modules,


            "time":

            str(datetime.now())

        }





if __name__=="__main__":



    print("="*50)

    print(
        "Football AI OS Governance Controller V1.0"
    )

    print("="*50)



    controller=GovernanceController()


    base=r"E:\football_v\03_Data_Governance"



    controller.check_module(

        "quality_engine",

        base+r"\quality\quality_engine.py"

    )


    controller.check_module(

        "validation_engine",

        base+r"\validation\validation_engine.py"

    )


    controller.check_module(

        "lineage_engine",

        base+r"\lineage\lineage_engine.py"

    )


    controller.check_module(

        "audit_engine",

        base+r"\audit\audit_engine.py"

    )



    result=controller.generate_status()



    print(

        json.dumps(

            result,

            indent=4,

            ensure_ascii=False

        )

    )



    with open(

        base+r"\reports\governance_status.json",

        "w",

        encoding="utf-8"

    ) as f:


        json.dump(

            result,

            f,

            indent=4,

            ensure_ascii=False

        )



