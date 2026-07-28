import json
import sys

sys.path.append(
r"E:\football_v\08_DECISION_INTELLIGENCE_LAYER\feedback_interface"
)

from feedback_connector import FeedbackConnector


source=r"E:\football_v\14_OPERATION_LAYER\output\prediction_result.json"


with open(source,"r",encoding="utf-8") as f:
    data=json.load(f)


connector=FeedbackConnector()

result=connector.feedback(data)


print(result)
