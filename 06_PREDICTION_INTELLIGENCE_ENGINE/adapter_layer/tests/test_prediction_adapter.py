from prediction_adapter import PredictionAdapter



def test_prediction_adapter():


    adapter = PredictionAdapter()


    result = adapter.predict(

        {

        "home":"A",

        "away":"B"

        }

    )


    assert result["status"] == "PREDICTION_ADAPTER_READY"


    assert "elo" in result["models"]

    assert "dixon_coles" in result["models"]

    assert "poisson" in result["models"]

    assert "xgboost" in result["models"]



    print(

        "Prediction Adapter PASS"

    )



if __name__=="__main__":

    test_prediction_adapter()

