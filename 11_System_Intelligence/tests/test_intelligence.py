import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)


from system_brain import SystemBrain



def test_brain():

    b = SystemBrain()

    assert b.status()["brain"]=="active"