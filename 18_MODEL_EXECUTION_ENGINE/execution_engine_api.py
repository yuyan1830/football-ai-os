
from module import ExecutionEngine


class ExecutionAPI:

    def __init__(self):

        self.engine=ExecutionEngine()


    def predict(self):

        return self.engine.predict()



if __name__=="__main__":

    api=ExecutionAPI()

    print(
        api.predict()
    )
