from pathlib import Path


ROOT = Path(r"E:\football_v")


FILES = {


"pytest.ini":

"""
[pytest]

testpaths =
    09_Prediction_System/tests
    11_System_Intelligence/tests

pythonpath =
    09_Prediction_System
    11_System_Intelligence
""",



"09_Prediction_System/__init__.py":

"""
""",


"09_Prediction_System/tests/__init__.py":

"""
""",


"11_System_Intelligence/__init__.py":

"""
""",


"11_System_Intelligence/tests/__init__.py":

"""
""",



"09_Prediction_System/tests/test_prediction_system.py":

"""
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)


from prediction_pipeline import PredictionPipeline



def test_prediction():

    p = PredictionPipeline()

    r = p.run("test")

    assert r["status"] == "processed"
""",



"11_System_Intelligence/tests/test_intelligence.py":

"""
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)


from system_brain import SystemBrain



def test_brain():

    b = SystemBrain()

    assert b.status()["brain"]=="active"
"""

}



for f,c in FILES.items():

    p = ROOT / f

    p.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    p.write_text(
        c.strip(),
        encoding="utf-8"
    )

    print("[PATCH]",p)


print()
print("Football AI OS V1.5 Phase1 Patch Complete")