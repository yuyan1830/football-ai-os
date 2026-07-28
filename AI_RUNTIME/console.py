from AI_RUNTIME.runtime import run


def start():

    print("================================")
    print(" Football AI OS ")
    print(" Frozen Framework V1.5 ")
    print("================================")

    while True:

        msg=input("> ")

        if msg=="exit":
            break

        result=run(msg)

        print(result)


if __name__=="__main__":
    start()

