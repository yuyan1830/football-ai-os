
import traceback


def handle_exception(error):

    return {

        "type":
            error.__class__.__name__,


        "message":
            str(error),


        "trace":
            traceback.format_exc()

    }



