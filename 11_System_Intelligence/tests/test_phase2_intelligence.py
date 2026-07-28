from system_analyzer import SystemAnalyzer



def test_system():

    s=SystemAnalyzer()

    assert s.analyze()["system"]=="healthy"