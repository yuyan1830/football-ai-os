"""
Football AI OS

Core Validator

Data Validator Service

Version:
V1.0
"""


import os


from .validation_result import ValidationResult




def validate_exists(path):


    result = ValidationResult(

        module="data_validator",

        target=path

    )


    exists = os.path.exists(path)


    result.details[

        "exists"

    ] = exists



    if not exists:


        result.add_error(

            "File does not exist"

        )


    return result





def validate_size(path):


    result = ValidationResult(

        module="data_validator",

        target=path

    )


    if not os.path.exists(path):


        result.add_error(

            "File does not exist"

        )


        return result



    size = os.path.getsize(path)



    result.details[

        "size"

    ] = size



    if size <= 0:


        result.add_error(

            "File is empty"

        )



    return result






def validate_file(path):


    result = ValidationResult(

        module="data_validator",

        target=path

    )



    exists_result = validate_exists(path)



    size_result = validate_size(path)



    if exists_result.errors:


        for error in exists_result.errors:


            result.add_error(

                error

            )



    if size_result.errors:


        for error in size_result.errors:


            result.add_error(

                error

            )



    result.details = {


        "exists":

            exists_result.details.get(

                "exists",

                False

            ),



        "size":

            size_result.details.get(

                "size",

                0

            )

    }



    return result