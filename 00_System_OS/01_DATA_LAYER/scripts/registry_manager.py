import sqlite3
import hashlib
import uuid
import datetime
import os


DB_PATH = (
r"E:\football_v\00_System_OS\01_DATA_LAYER"
r"\database\football_ai_os.db"
)



def calculate_hash(file_path):

    sha256 = hashlib.sha256()


    with open(
        file_path,
        "rb"
    ) as f:


        for chunk in iter(
            lambda:f.read(4096),
            b""
        ):

            sha256.update(chunk)


    return sha256.hexdigest()



def register_file(

        file_path,

        data_type,

        source

):


    file_hash = calculate_hash(
        file_path
    )


    conn = sqlite3.connect(
        DB_PATH
    )


    cursor = conn.cursor()



    data_id = str(
        uuid.uuid4()
    )


    now = datetime.datetime.now().isoformat()



    cursor.execute(
    """

    INSERT INTO data_registry

    (

    data_id,

    file_name,

    file_path,

    data_type,

    source,

    hash,

    version,

    status,

    created_time

    )


    VALUES

    (?,?,?,?,?,?,?,?,?)

    """,

    (

    data_id,

    os.path.basename(file_path),

    file_path,

    data_type,

    source,

    file_hash,

    "v001",

    "verified",

    now

    )

    )


    conn.commit()

    conn.close()



    print(
        "[REGISTERED]",
        data_id
    )



if __name__ == "__main__":


    register_file(

        "test.csv",

        "market_odds",

        "manual"

    )