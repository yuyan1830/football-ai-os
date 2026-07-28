# -*- coding:utf-8 -*-

"""
Football AI OS
Data Validation Engine
Version V1.0
"""


import os
import json
from datetime import datetime



class ValidationEngine:


    def __init__(self):

        self.results=[]



    def add_result(self,name,result):

        self.results.append(

            {
                "rule":name,
                "result":result
            }

        )



    def validate_file(self,path):


        exists=os.path.exists(path)


        self.add_result(

            "file_exists",

            exists

        )


        return exists




    def validate_json(self,path):


        try:

            with open(
                path,
                "r",
                encoding="utf-8-sig"
            ) as f:


                json.load(f)


            result=True


        except Exception:


            result=False



        self.add_result(

            "json_format",

            result

        )


        return result





    def report(self):


        passed=sum(

            1 for x in self.results

            if x["result"]

        )


        total=len(self.results)



        score=0


        if total:

            score=int(
                passed/total*100
            )



        return {


            "framework":
            "Football AI OS",


            "module":
            "03_DATA_GOVERNANCE",


            "service":
            "validation_engine",


            "version":
            "V1.0",


            "score":
            score,


            "status":
            "PASS" if score==100 else "WARNING",


            "checks":
            self.results,


            "time":
            str(datetime.now())

        }




if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Validation Engine V1.0"
    )

    print("="*50)



    engine=ValidationEngine()



    engine.validate_file(

        r"E:\football_v\03_Data_Governance\quality\quality_engine.py"

    )



    engine.validate_json(

        r"E:\football_v\03_Data_Governance\registry\quality_registry.json"

    )



    report=engine.report()



    print(

        json.dumps(

            report,

            indent=4,

            ensure_ascii=False

        )

    )



    with open(

        r"E:\football_v\03_Data_Governance\reports\validation_report.json",

        "w",

        encoding="utf-8"

    ) as f:


        json.dump(

            report,

            f,

            indent=4,

            ensure_ascii=False

        )



