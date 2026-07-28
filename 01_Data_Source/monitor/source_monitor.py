# -*- coding: utf-8 -*-

"""
Football AI OS
Data Source Monitor V1.0
"""

import os
import json
import datetime


BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)


REGISTRY_FILE = os.path.join(
    BASE_DIR,
    "registry",
    "source_registry.json"
)


DOWNLOAD_PATH = os.path.join(
    BASE_DIR,
    "download"
)


REPORT_FILE = os.path.join(
    os.path.dirname(__file__),
    "source_health_report.json"
)



class SourceMonitor:


    def __init__(self):

        self.result = {
            "version": "V1.0",
            "time": str(datetime.datetime.now()),
            "sources": []
        }



    def load_registry(self):

        with open(
            REGISTRY_FILE,
            "r",
            encoding="utf-8-sig"
        ) as f:

            return json.load(f)



    def check_download_folder(self):

        exists = os.path.exists(
            DOWNLOAD_PATH
        )


        files = []

        if exists:

            files = os.listdir(
                DOWNLOAD_PATH
            )


        return {
            "path": DOWNLOAD_PATH,
            "exists": exists,
            "file_count": len(files)
        }



    def run(self):

        registry = self.load_registry()


        folder_status = (
            self.check_download_folder()
        )


        for source in registry["sources"]:

            item = {

                "name":
                source["name"],

                "type":
                source["type"],

                "status":
                source["status"],

                "download_check":
                folder_status

            }


            self.result["sources"].append(
                item
            )


        self.save()


        return self.result



    def save(self):

        with open(
            REPORT_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.result,
                f,
                indent=4,
                ensure_ascii=False
            )



if __name__ == "__main__":


    print("="*50)

    print(
        "Football AI OS Source Monitor V1.0"
    )

    print("="*50)


    monitor = SourceMonitor()


    result = monitor.run()


    print(
        json.dumps(
            result,
            indent=4,
            ensure_ascii=False
        )
    )


    print()

    print(
        "Health report generated:"
    )

    print(
        REPORT_FILE
    )