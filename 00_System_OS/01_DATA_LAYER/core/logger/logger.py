import logging
import json
import os

from .handlers import (
    create_file_handler,
    create_console_handler
)


CONFIG_PATH = os.path.join(
    os.path.dirname(__file__),
    "log_config.json"
)


_LOGGERS = {}



def load_config():

    if not os.path.exists(
        CONFIG_PATH
    ):
        return {
            "level": "INFO",
            "file": "logs/football_ai.log",
            "console": True
        }


    with open(
        CONFIG_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def get_logger(
        name
):

    if name in _LOGGERS:
        return _LOGGERS[name]


    config = load_config()


    logger = logging.getLogger(
        name
    )


    level = getattr(
        logging,
        config.get(
            "level",
            "INFO"
        )
    )


    logger.setLevel(
        level
    )


    logger.propagate = False


    if not logger.handlers:


        if config.get(
            "console",
            True
        ):

            logger.addHandler(
                create_console_handler()
            )


        logger.addHandler(
            create_file_handler(
                config.get(
                    "file"
                )
            )
        )


    _LOGGERS[name] = logger


    return logger


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

