
from football_ai_runtime import FootballAIRuntime


def test_runtime():

    e=FootballAIRuntime()

    assert e.start()==True
