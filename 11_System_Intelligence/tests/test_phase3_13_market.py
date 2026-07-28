
from les_engine import LESEngine


def test_les():

    e=LESEngine()

    r=e.calculate(
        0
    )

    assert r["LES"]==80
