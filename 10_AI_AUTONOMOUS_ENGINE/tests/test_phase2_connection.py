from intelligence_connector import IntelligenceConnector



def test_connector():

    c=IntelligenceConnector()

    r=c.feedback("test")

    assert r["connected"]==True