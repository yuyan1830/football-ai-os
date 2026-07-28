import os
import shutil



def ensure_folder(path):

    os.makedirs(
        path,
        exist_ok=True
    )



def move_file(
    source,
    target
):

    ensure_folder(
        os.path.dirname(target)
    )


    shutil.move(
        source,
        target
    )


    return True



def file_exists(path):

    return os.path.exists(
        path
    )