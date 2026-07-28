
from monte_carlo_engine import MonteCarloEngine


def test_simulation():

    m=MonteCarloEngine()

    r=m.simulate()

    assert r["count"]==10000
