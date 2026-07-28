import os
import datetime


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


LOG_DIR = os.path.join(
    BASE_DIR,
    "logs"
)


os.makedirs(
    LOG_DIR,
    exist_ok=True
)



def write_log(level, message):

    today = datetime.datetime.now().strftime(
        "%Y-%m-%d"
    )


    log_file = os.path.join(
        LOG_DIR,
        today + ".log"
    )


    timestamp = datetime.datetime.now().isoformat()


    content = (
        f"{timestamp} "
        f"[{level}] "
        f"{message}\n"
    )


    with open(
        log_file,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(content)



    return True