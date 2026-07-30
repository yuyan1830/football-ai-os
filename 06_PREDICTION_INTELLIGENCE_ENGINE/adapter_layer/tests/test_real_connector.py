from prediction_adapter import PredictionAdapter



def test_real_connector():


    adapter=PredictionAdapter()


    result=adapter.predict(

        {

        "home":"A",

        "away":"B"

        }

    )


    assert result["models"]["elo"]=="Elo"

    assert result["models"]["dixon_coles"]=="Dixon-Coles"

    assert result["models"]["poisson"]=="Poisson"

    assert result["models"]["xgboost"]=="XGBoost"



    assert result["status"]=="REAL_CONNECTOR_READY"



    print(

        "Prediction Adapter Real Connector PASS"

    )



if __name__=="__main__":

    test_real_connector()

