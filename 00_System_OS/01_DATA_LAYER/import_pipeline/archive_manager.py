import shutil
import os



def archive_file(

    source,

    target

):


    os.makedirs(

        os.path.dirname(target),

        exist_ok=True

    )


    shutil.copy2(

        source,

        target

    )


    return True