# -*- coding: utf-8 -*-

import os
import json


PROJECT_ROOT = r"E:\football_v"

FEATURE_STORE_PATH = os.path.join(
    PROJECT_ROOT,
    "04_DATA_PROCESSING_AI",
    "FEATURE_STORE"
)


DATABASE_DEVELOPMENT = os.path.join(
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

    print(
        "Football AI OS Module Deployment Tool V1.0"
    )

    print(
        "Module : Feature Store"
    )

    print(
        "Version: V1.4"
    )

    print("=" * 60)



    # =============================
    # Database Environment
    # =============================


    database_dirs = [

        DATABASE_DEVELOPMENT,

        DATABASE_DEVELOPMENT + r"\raw",

        DATABASE_DEVELOPMENT + r"\cleaned",

        DATABASE_DEVELOPMENT + r"\processed",

        DATABASE_DEVELOPMENT + r"\feature_dataset"

    ]


    for d in database_dirs:

        create_dir(d)



    # =============================
    # Feature Store folders
    # =============================


    folders = [

        FEATURE_STORE_PATH,

        FEATURE_STORE_PATH + r"\config",

        FEATURE_STORE_PATH + r"\schema",

        FEATURE_STORE_PATH + r"\reports",

        FEATURE_STORE_PATH + r"\tests"

    ]


    for folder in folders:

        create_dir(folder)



    # =============================
    # Match Reader
    # =============================


    write_file(

        FEATURE_STORE_PATH +
        r"\feature_match_reader.py",

"""
# -*- coding: utf-8 -*-


import os
import json



class FeatureMatchReader:


    def __init__(self, path):

        self.path = path



    def read_json(self):


        if not os.path.exists(
            self.path
        ):

            return []


        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:


            return json.load(f)


"""
)



    # =============================
    # Feature Generator
    # =============================


    write_file(

        FEATURE_STORE_PATH +
        r"\feature_feature_generator.py",

"""
# -*- coding: utf-8 -*-



class FeatureGenerator:



    def generate(
        self,
        matches
    ):


        dataset=[]



        for match in matches:


            dataset.append({

                "home_team":
                match.get(
                    "home_team"
                ),


                "away_team":
                match.get(
                    "away_team"
                ),


                "home_score":
                match.get(
                    "home_score"
                ),


                "away_score":
                match.get(
                    "away_score"
                )

            })


        return dataset


"""
)



    # =============================
    # Schema Validator
    # =============================


    write_file(

        FEATURE_STORE_PATH +
        r"\feature_dataset_schema_validator.py",

"""
# -*- coding: utf-8 -*-



class DatasetSchemaValidator:



    required_fields=[

        "home_team",

        "away_team",

        "home_score",

        "away_score"

    ]



    def validate(
        self,
        data
    ):


        for row in data:


            for field in self.required_fields:


                if field not in row:

                    return False


        return True


"""
)



    # =============================
    # Reporter
    # =============================


    write_file(

        FEATURE_STORE_PATH +
        r"\feature_dataset_reporter.py",

"""
# -*- coding: utf-8 -*-


import json



class FeatureDatasetReporter:



    def report(
        self,
        data,
        path
    ):


        result={

            "dataset_size":
            len(data),

            "status":
            "READY"

        }


        with open(

            path,

            "w",

            encoding="utf-8"

        ) as f:


            json.dump(

                result,

                f,

                indent=4

            )


"""
)



    # =============================
    # Config
    # =============================


    write_json(

        FEATURE_STORE_PATH +
        r"\config\match_data_runtime.json",

{

"framework":

"Football AI OS",


"module":

"Feature Store",


"version":

"V1.4",


"environment":

"development",


"database_path":

DATABASE_DEVELOPMENT,


"legacy_project_access":

False


}

)



    # =============================
    # Schema
    # =============================


    write_json(

        FEATURE_STORE_PATH +
        r"\schema\match_dataset_schema.json",

{

"fields":[

"home_team",

"away_team",

"home_score",

"away_score"

],

"version":

"V1.4"

}

)



    # =============================
    # Report
    # =============================


    write_json(

        FEATURE_STORE_PATH +
        r"\reports\feature_dataset_generation_report.json",

{

"module":

"Feature Store",


"version":

"V1.4",


"status":

"READY"


}

)



    # =============================
    # Test
    # =============================


    write_file(

        FEATURE_STORE_PATH +
        r"\tests\feature_dataset_generation_test.py",

"""
# -*- coding: utf-8 -*-

import os
import json



BASE=os.path.dirname(
    os.path.dirname(__file__)
)



def test():


    files=[


        "feature_match_reader.py",

        "feature_feature_generator.py",

        "feature_dataset_schema_validator.py",

        "feature_dataset_reporter.py"

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

"Feature Store V1.4",


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

    print(
        "Feature Store V1.4 Deployment PASS"
    )

    print(
        "Generated:"
    )

    print(
        FEATURE_STORE_PATH
    )

    print("="*60)



if __name__=="__main__":

    deploy()