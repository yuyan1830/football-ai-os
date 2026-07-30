from command_router import route
from api_connector import call_system



def process(message):


    task = route(
        message
    )


    return call_system(
        task,
        message
    )

