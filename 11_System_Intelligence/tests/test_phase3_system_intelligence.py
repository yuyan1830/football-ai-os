from intelligence_controller import IntelligenceController



def test_controller_health():

    engine=IntelligenceController()

    result=engine.health_check()

    assert result["status"]=="PASS"



def test_controller_execute():

    engine=IntelligenceController()

    result=engine.execute(
        {
            "task":"football_prediction"
        }
    )


    assert result["status"]=="PASS"


    assert result["analysis"]["reasoning"]=="completed"