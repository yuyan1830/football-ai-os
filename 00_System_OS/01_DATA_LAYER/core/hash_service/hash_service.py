
import hashlib
import os
from datetime import datetime


try:

    from core.logger import logger

except:

    logger=None





def calculate_hash(

        file_path,

        algorithm="sha256"

):


    if not os.path.exists(file_path):

        raise FileNotFoundError(

            file_path

        )



    hash_object = hashlib.new(

        algorithm

    )



    with open(

        file_path,

        "rb"

    ) as f:



        for block in iter(

            lambda:

            f.read(4096),

            b""

        ):


            hash_object.update(

                block

            )




    result = hash_object.hexdigest()



    if logger:

        logger.info(

            f"Hash calculated: {file_path}"

        )



    return result






def verify_hash(

        file_path,

        expected_hash,

        algorithm="sha256"

):


    current_hash = calculate_hash(

        file_path,

        algorithm

    )


    return current_hash == expected_hash







def hash_info(

        file_path,

        algorithm="sha256"

):


    return {


        "file":

        file_path,


        "exists":

        os.path.exists(file_path),


        "algorithm":

        algorithm,


        "hash":

        calculate_hash(

            file_path,

            algorithm

        ) if os.path.exists(file_path)

        else None,


        "time":

        datetime.now().isoformat()

    }





if __name__=="__main__":


    print(

        "Hash Service V1.1 Ready"

    )


