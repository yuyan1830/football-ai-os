import os



def validate_file(path):


    result={}


    result["exists"] = os.path.exists(
        path
    )


    if result["exists"]:


        size=os.path.getsize(
            path
        )


        result["size"]=size


        result["valid"]=size>0


    else:

        result["valid"]=False


    return result