
import os
import json
from datetime import datetime



try:

    from core.logger import logger

except:

    logger=None





SYSTEM_VERSION="Football_AI_OS_V1.1"





def get_system_version():


    return {


        "system":

        SYSTEM_VERSION,


        "time":

        datetime.now().isoformat()


    }








def get_module_version(

        module_name,

        version="V1.1"

):


    return {


        "module":

        module_name,


        "version":

        version,


        "time":

        datetime.now().isoformat()


    }








def save_version_record(

        path,

        data

):


    records=[]


    if os.path.exists(path):


        with open(

            path,

            "r",

            encoding="utf-8"

        ) as f:


            try:

                records=json.load(f)

            except:

                records=[]



    records.append(data)



    with open(

        path,

        "w",

        encoding="utf-8"

    ) as f:


        json.dump(

            records,

            f,

            ensure_ascii=False,

            indent=4

        )



    if logger:


        logger.info(

            "Version record saved"

        )





def version_check():


    return {


        "service":

        "Version Service",


        "status":

        "OK",


        "version":

        SYSTEM_VERSION


    }






if __name__=="__main__":


    print(

        version_check()

    )


