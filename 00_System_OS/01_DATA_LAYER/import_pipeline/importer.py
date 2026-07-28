import os


from core.hash_service import calculate_hash


from registry.registry_manager import register_data


from import_pipeline.duplicate_checker import check_duplicate


from import_pipeline.validator import validate_file



def import_file(

    file_path,

    data_type,

    source

):


    print(
        "Import:",
        file_path
    )


    file_hash = calculate_hash(
        file_path
    )


    print(
        "Hash:",
        file_hash
    )



    duplicate = check_duplicate(
        file_hash
    )


    if duplicate["duplicate"]:


        print(
            "Duplicate:",
            duplicate["data_id"]
        )


        return {


            "status":
            "duplicate",


            "data_id":
            duplicate["data_id"],


            "file_hash":
            file_hash,


            "message":
            "File already registered"

        }



    check = validate_file(
        file_path
    )



    if not check["valid"]:


        return {


            "status":
            "failed",


            "message":
            "Invalid file"

        }




    data_id = register_data(

        file_name=os.path.basename(
            file_path
        ),

        file_hash=file_hash,

        data_type=data_type,

        source=source

    )



    return {


        "status":
        "success",


        "data_id":
        data_id,


        "file_name":
        os.path.basename(
            file_path
        ),


        "file_hash":
        file_hash,


        "data_type":
        data_type,


        "source":
        source,


        "version":
        "v001",


        "message":
        "Data registered successfully"

    }