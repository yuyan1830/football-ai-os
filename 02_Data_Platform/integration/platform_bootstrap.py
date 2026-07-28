# -*- coding: utf-8 -*-

"""
Football AI OS
Data Platform Bootstrap
V1.0
"""


import os
import json
from datetime import datetime



class PlatformBootstrap:


    def __init__(self):

        self.root = os.path.dirname(
            os.path.dirname(__file__)
        )



    def check_file(self, path):

        return os.path.exists(
            os.path.join(
                self.root,
                path
            )
        )



    def health_check(self):


        services = {


            "raw_layer":
            self.check_file(
                "raw/raw_registry.json"
            ),


            "storage_engine":
            self.check_file(
                "storage_engine/storage_registry.json"
            ),


            "loader_engine":
            self.check_file(
                "data_loader/engine/loader_engine.py"
            ),


            "pipeline":
            self.check_file(
                "pipeline/data_pipeline.py"
            ),


            "data_manager":
            self.check_file(
                "data_manager/data_manager.py"
            ),


            "metadata":
            self.check_file(
                "metadata/metadata_manager.py"
            ),


            "lineage":
            self.check_file(
                "metadata/lineage/data_lineage.py"
            )

        }


        status = all(
            services.values()
        )


        return {


            "framework":
            "Football AI OS",


            "module":
            "02_DATA_PLATFORM",


            "version":
            "V1.0",


            "services":
            len(services),


            "health":
            "PASS" if status else "FAIL",


            "details":
            services,


            "time":
            str(datetime.now())

        }



if __name__=="__main__":


    print("="*60)

    print(
        "Football AI OS Data Platform Bootstrap V1.0"
    )

    print("="*60)



    boot=PlatformBootstrap()


    report=boot.health_check()



    print(
        json.dumps(
            report,
            indent=4,
            ensure_ascii=False
        )
    )