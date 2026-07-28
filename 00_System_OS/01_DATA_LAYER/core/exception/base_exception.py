
class FootballAIException(Exception):


    def __init__(

        self,

        message,

        code="SYSTEM_ERROR"

    ):


        self.message = message

        self.code = code


        super().__init__(message)



    def to_dict(self):


        return {


            "error":

            self.code,


            "message":

            self.message


        }

