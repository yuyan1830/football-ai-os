
from .base_exception import FootballAIException



class ValidationException(FootballAIException):


    def __init__(self,message):


        super().__init__(

            message,

            "VALIDATION_ERROR"

        )

