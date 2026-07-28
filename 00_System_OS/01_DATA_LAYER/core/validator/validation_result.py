"""
Football AI OS

Core Validator

Validation Result Object

Version:
V1.0
"""


from datetime import datetime



class ValidationResult:


    def __init__(

        self,

        status="PASS",

        module="validator",

        target=None,

        errors=None,

        warnings=None,

        details=None

    ):


        self.status = status

        self.module = module

        self.target = target


        self.errors = errors or []

        self.warnings = warnings or []

        self.details = details or {}


        self.created_time = (

            datetime.now()

            .isoformat()

        )



    def add_error(

        self,

        message

    ):


        self.errors.append(

            message

        )


        self.status = "FAIL"



    def add_warning(

        self,

        message

    ):


        self.warnings.append(

            message

        )



    def success(self):

        return self.status == "PASS"



    def to_dict(self):


        return {


            "status":

                self.status,


            "module":

                self.module,


            "target":

                self.target,


            "errors":

                self.errors,


            "warnings":

                self.warnings,


            "details":

                self.details,


            "created_time":

                self.created_time

        }



    def __repr__(self):

        return str(

            self.to_dict()

        )