
class FootballAIException(Exception):

    def __init__(
        self,
        message,
        code=None
    ):

        self.message = message
        self.code = code

        super().__init__(message)



class DatabaseException(FootballAIException):
    pass



class FileException(FootballAIException):
    pass



class ValidationException(FootballAIException):
    pass



class PipelineException(FootballAIException):
    pass


