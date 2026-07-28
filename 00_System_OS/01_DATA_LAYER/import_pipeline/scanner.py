import os



def scan_folder(folder):


    files=[]


    for root,dirs,names in os.walk(folder):

        for name in names:


            path=os.path.join(
                root,
                name
            )


            files.append(
                path
            )


    return files



if __name__=="__main__":

    print(
        scan_folder(
            "../raw_data"
        )
    )