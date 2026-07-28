
from evolution_engine import EvolutionEngine



def test_evolution_engine():

    engine=EvolutionEngine()


    result=engine.evolve(
        0.8,
        1
    )


    assert result["error"]==0.2

    assert result["score"]==0.8



def test_evolution_rule():

    engine=EvolutionEngine()


    result=engine.evolve(
        0.1,
        1
    )


    assert "rule" in result
