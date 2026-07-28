
from .logger import get_logger


def write_log(level, message):

    logger = get_logger(
        "Football_AI_OS"
    )


    level = str(level).upper()


    if level == "ERROR":

        logger.error(
            message
        )

    elif level == "WARNING":

        logger.warning(
            message
        )

    else:

        logger.info(
            message
        )


    return True
