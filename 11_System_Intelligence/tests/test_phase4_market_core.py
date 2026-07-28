
from les_advanced import LESAdvanced


def test_les():

    l=LESAdvanced()

    r=l.calculate({})

    assert r["LES"]==85

