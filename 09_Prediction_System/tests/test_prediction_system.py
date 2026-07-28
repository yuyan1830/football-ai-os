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