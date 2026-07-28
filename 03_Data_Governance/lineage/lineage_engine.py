# -*- coding:utf-8 -*-

"""
Football AI OS
Data Lineage Engine
Version V1.0
"""


import json
from datetime import datetime



class LineageEngine:


    def __init__(self):

        self.nodes=[]



    def add_flow(self,source,target,flow_type):

        self.nodes.append(

            {

                "source":source,

                "target":target,

                "type":flow_type

            }

        )



    def report(self):

        return {


            "framework":

            "Football AI OS",


            "module":

            "03_DATA_GOVERNANCE",


            "service":

            "lineage_engine",


            "version":

            "V1.0",


            "status":

            "PASS",


            "flows":

            self.nodes,


            "time":

            str(datetime.now())

        }





if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Data Lineage Engine V1.0"
    )

    print("="*50)



    engine=LineageEngine()



    engine.add_flow(

        "01_DATA_SOURCE",

        "02_DATA_PLATFORM",

        "raw_import"

    )


    engine.add_flow(

        "02_DATA_PLATFORM",

        "03_DATA_GOVERNANCE",

        "quality_validation"

    )


    engine.add_flow(

        "03_DATA_GOVERNANCE",

        "07_MODEL_ENGINE",

        "feature_delivery"

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

        r"E:\football_v\03_Data_Governance\reports\lineage_report.json",

        "w",

        encoding="utf-8"

    ) as f:


        json.dump(

            report,

            f,

            indent=4,

            ensure_ascii=False

        )


