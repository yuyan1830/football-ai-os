import logging


class FootballFormatter(logging.Formatter):

    def __init__(self):

        super().__init__(
            fmt=(
                "%(asctime)s | "
                "%(levelname)s | "
                "%(name)s | "
                "%(message)s"
            ),
            datefmt="%Y-%m-%d %H:%M:%S"
        )