# -*- coding: utf-8 -*-

"""
Football AI OS
Data Source Download Engine V1.1
"""


import os
import json
import hashlib
import datetime



BASE_DIR = os.path.dirname(__file__)


HISTORY_FILE = os.path.join(
    BASE_DIR,
    "download_history.json"
)



class DataDownloader:


    def __init__(self):

        self.history = self.load_history()



    def load_history(self):

        if not os.path.exists(
            HISTORY_FILE
        ):

            return {
                "history":[]
            }


        with open(
            HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



    def calculate_hash(
        self,
        file_path
    ):

        sha256 = hashlib.sha256()


        with open(
            file_path,
            "rb"
        ) as f:


            for block in iter(
                lambda:
                f.read(4096),
                b""
            ):

                sha256.update(block)


        return sha256.hexdigest()



    def scan_files(self):

        files=[]


        for root,dirs,names in os.walk(
            BASE_DIR
        ):

            for name in names:

                if name.endswith(
                    ".csv"
                ):

                    path=os.path.join(
                        root,
                        name
                    )


                    files.append(
                        {
                            "file":
                            name,

                            "hash":
                            self.calculate_hash(path)
                        }
                    )


        return files



    def record(self):

        record={

            "time":
            str(datetime.datetime.now()),


            "files":
            self.scan_files(),


            "status":
            "completed"

        }


        self.history["history"].append(
            record
        )


        self.save()



        return record



    def save(self):

        with open(
            HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.history,
                f,
                indent=4,
                ensure_ascii=False
            )



if __name__=="__main__":


    print("="*50)

    print(
        "Football AI OS Download Engine V1.1"
    )

    print("="*50)



    engine=DataDownloader()


    result=engine.record()


    print(
        json.dumps(
            result,
            indent=4,
            ensure_ascii=False
        )
    )


    print()

    print(
        "Download history updated"
    )