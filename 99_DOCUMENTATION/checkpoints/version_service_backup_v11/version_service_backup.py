import os



def generate_version_name(

    folder,

    filename

):


    name, ext = os.path.splitext(
        filename
    )


    version = 1


    while True:


        new_name = (

            f"{name}_v"
            f"{version:03d}"
            f"{ext}"

        )


        new_path = os.path.join(
            folder,
            new_name
        )


        if not os.path.exists(
            new_path
        ):

            return new_name


        version += 1