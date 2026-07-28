
import os
import shutil
from datetime import datetime



# Logger integration

try:

    from core.logger import logger

except:

    logger=None



# Exception integration

try:

    from core.exception import FileServiceException

except:


    class FileServiceException(Exception):

        pass





def ensure_folder(path):


    try:

        os.makedirs(

            path,

            exist_ok=True

        )


        if logger:

            logger.info(
                f"Folder created or exists: {path}"
            )


        return True



    except Exception as e:


        if logger:

            logger.error(
                str(e)
            )


        raise FileServiceException(
            str(e)
        )







def move_file(

    source,

    target

):


    try:


        if not os.path.exists(source):

            raise FileServiceException(

                f"Source file missing: {source}"

            )


        folder=os.path.dirname(target)


        if folder:

            ensure_folder(folder)



        shutil.move(

            source,

            target

        )



        if logger:

            logger.info(

                f"Moved file: {source} -> {target}"

            )



        return {


            "status":

            "success",


            "source":

            source,


            "target":

            target,


            "time":

            datetime.now().isoformat()

        }



    except Exception as e:


        if logger:

            logger.error(

                str(e)

            )


        raise FileServiceException(

            str(e)

        )







def file_exists(path):


    result=os.path.exists(path)


    return result





def file_info(path):


    if not os.path.exists(path):

        return {


            "exists":

            False

        }



    return {


        "exists":

        True,


        "size":

        os.path.getsize(path),


        "modified":

        datetime.fromtimestamp(

            os.path.getmtime(path)

        ).isoformat()

    }






if __name__=="__main__":


    print(

        "File Service V1.1 Ready"

    )


