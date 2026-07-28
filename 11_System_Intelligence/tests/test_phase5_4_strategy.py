
from single_strategy import SingleStrategy


def test_strategy():

    s=SingleStrategy()

    assert s.run()=="single"
