
from .base_exception import FootballAIException



class DatabaseException(FootballAIException):


    def __init__(self,message):


        super().__init__(

            message,

            "DATABASE_ERROR"

        )

