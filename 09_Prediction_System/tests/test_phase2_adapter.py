from model_result_adapter import ModelResultAdapter



def test_adapter():

    a=ModelResultAdapter()

    r=a.adapt("model")

    assert r["status"]=="adapted"