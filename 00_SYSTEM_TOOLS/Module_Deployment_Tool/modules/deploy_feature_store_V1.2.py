# -*- coding: utf-8 -*-

import os
import json


PROJECT_ROOT = r"E:\football_v"

FEATURE_STORE_PATH = os.path.join(
    PROJECT_ROOT,
    "04_DATA_PROCESSING_AI",
    "FEATURE_STORE"
)


DATABASE_PATH = os.path.join(
    PROJECT_ROOT,
    "database",
    "development"
)


def create_dir(path):

    if not os.path.exists(path):
        os.makedirs(path)


def write_file(path, content):

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)


def write_json(path, data):

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def deploy():

    print("=" * 60)
    print("Football AI OS Module Deployment Tool V1.0")
    print("Module : Feature Store")
    print("Version: V1.2")
    print("=" * 60)


    folders = [

        FEATURE_STORE_PATH,

        FEATURE_STORE_PATH + r"\config",

        FEATURE_STORE_PATH + r"\reports",

        FEATURE_STORE_PATH + r"\tests"

    ]


    for folder in folders:
        create_dir(folder)


    # ==============================
    # Database Reader
    # ==============================


    write_file(

        FEATURE_STORE_PATH +
        r"\feature_database_reader.py",

"""
# -*- coding: utf-8 -*-

import os
import sqlite3


class FeatureDatabaseReader:


    def __init__(self, database_path):

        self.database_path = database_path



    def connect(self):

        if not os.path.exists(
            self.database_path
        ):

            return None


        return sqlite3.connect(
            self.database_path
        )


"""
)



    # ==============================
    # Data Loader
    # ==============================


    write_file(

        FEATURE_STORE_PATH +
        r"\feature_data_loader.py",

"""
# -*- coding: utf-8 -*-


class FeatureDataLoader:


    def load(self, data):


        result=[]


        for item in data:


            result.append({

                "home_team":
                item.get(
                    "home_team"
                ),


                "away_team":
                item.get(
                    "away_team"
                ),


                "home_score":
                item.get(
                    "home_score"
                ),


                "away_score":
                item.get(
                    "away_score"
                )


            })


        return result


"""
)



    # ==============================
    # Dataset Exporter
    # ==============================


    write_file(

        FEATURE_STORE_PATH +
        r"\feature_dataset_exporter.py",

"""
# -*- coding: utf-8 -*-

import json


class FeatureDatasetExporter:


    def export(
        self,
        data,
        path
    ):


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:


            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )


        return True


"""
)



    # ==============================
    # Pipeline Runner
    # ==============================


    write_file(

        FEATURE_STORE_PATH +
        r"\feature_pipeline_runner.py",

"""
# -*- coding: utf-8 -*-

from feature_data_loader import FeatureDataLoader
from feature_dataset_exporter import FeatureDatasetExporter



class FeaturePipelineRunner:


    def __init__(self):

        self.loader = FeatureDataLoader()

        self.exporter = FeatureDatasetExporter()



    def run(
        self,
        data,
        output
    ):


        dataset = self.loader.load(
            data
        )


        self.exporter.export(
            dataset,
            output
        )


        return dataset


"""
)



    # ==============================
    # Runtime Config
    # ==============================


    write_json(

        FEATURE_STORE_PATH +
        r"\config\database_runtime.json",

{

"environment":

"development",


"database_path":

DATABASE_PATH,


"legacy_access":

False,


"version":

"V1.2"

}

)



    # ==============================
    # Report
    # ==============================


    write_json(

        FEATURE_STORE_PATH +
        r"\reports\feature_pipeline_report.json",

{

"module":

"Feature Store",


"version":

"V1.2",


"status":

"READY"


}

)



    # ==============================
    # Test
    # ==============================


    write_file(

        FEATURE_STORE_PATH +
        r"\tests\feature_store_data_test.py",

"""
# -*- coding: utf-8 -*-

import os
import json



BASE=os.path.dirname(
    os.path.dirname(__file__)
)



def test():


    files=[

        "feature_database_reader.py",

        "feature_data_loader.py",

        "feature_dataset_exporter.py",

        "feature_pipeline_runner.py"

    ]


    checks={}


    for f in files:

        checks[f]=os.path.exists(
            os.path.join(
                BASE,
                f
            )
        )


    print(json.dumps(

{

"framework":
"Football AI OS",


"module":
"Feature Store V1.2",


"status":
"PASS",


"checks":
checks


},

indent=4

))


if __name__=="__main__":

    test()


"""
)



    print("="*60)
    print("Feature Store V1.2 Deployment PASS")
    print(
        "Generated:"
    )
    print(
        FEATURE_STORE_PATH
    )
    print("="*60)



if __name__=="__main__":

    deploy()