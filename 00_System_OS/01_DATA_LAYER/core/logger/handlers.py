import logging
import os

from .formatter import FootballFormatter


def create_file_handler(
        log_file
):

    os.makedirs(
        os.path.dirname(log_file),
        exist_ok=True
    )

    handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )

    handler.setFormatter(
        FootballFormatter()
    )

    return handler



def create_console_handler():

    handler = logging.StreamHandler()

    handler.setFormatter(
        FootballFormatter()
    )

    return handler