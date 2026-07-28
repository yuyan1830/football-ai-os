import os


BASE_PATH = r"E:\football_v\00_System_OS\01_DATA_LAYER"


DIRECTORIES = [

    "database",

    "raw_data",
    "raw_data/match",
    "raw_data/team",
    "raw_data/player",

    "raw_data/market",
    "raw_data/market/odds_1x2",
    "raw_data/market/handicap",
    "raw_data/market/over_under",
    "raw_data/market/correct_score",
    "raw_data/market/exchange",

    "raw_data/external",

    "processed_data",

    "archive",

    "registry",

    "logs",

    "scripts"

]


def create_directories():

    for folder in DIRECTORIES:

        path = os.path.join(BASE_PATH, folder)

        os.makedirs(
            path,
            exist_ok=True
        )

        print(
            "[CREATED]",
            path
        )


if __name__ == "__main__":

    create_directories()

    print(
        "\nFootball AI OS Data Layer V1.0 Directory Ready"
    )