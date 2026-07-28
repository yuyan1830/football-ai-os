# -*- coding: utf-8 -*-

"""
Football AI OS
Data Quality Engine
Version V1.0
"""


import os
import json
from datetime import datetime



class QualityEngine:


    def __init__(self):

        self.results=[]



    def check_exists(self,path):

        result=os.path.exists(path)

        self.results.append(
            {
                "check":"file_exists",
                "path":path,
                "result":result
            }
        )

        return result



    def calculate_score(self):

        total=len(self.results)

        passed=sum(
            1 for x in self.results
            if x["result"]
        )

        if total==0:
            return 0

        return int(
            passed/total*100
        )



    def report(self):

        return {

            "framework":
            "Football AI OS",

            "module":
            "03_DATA_GOVERNANCE",

            "service":
            "quality_engine",

            "version":
            "V1.0",

            "score":
            self.calculate_score(),

            "status":
            "PASS",

            "checks":
            self.results,

            "time":
            str(datetime.now())

        }



if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Quality Engine V1.0"
    )

    print("="*50)



    engine=QualityEngine()



    engine.check_exists(
        r"E:\football_v\02_Data_Platform"
    )


    engine.check_exists(
        r"E:\football_v\01_Data_Source"
    )



    report=engine.report()



    print(
        json.dumps(
            report,
            indent=4,
            ensure_ascii=False
        )
    )



    output=(
    r"E:\football_v\03_Data_Governance\reports\quality_report.json"
    )



    with open(
        output,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(
            report,
            f,
            indent=4,
            ensure_ascii=False
        )



    print()

    print(
        "Report Saved:"
    )

    print(output)

