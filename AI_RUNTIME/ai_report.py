def generate_report(prediction,decision):


    return {

        "system":
            "Football AI OS",

        "match":
            prediction["match"],

        "model_result":
            prediction["fusion"],

        "final_decision":
            decision.get(
                "final_decision",
                {}
            ),

        "decision_layer":
            decision.get(
                "decision_layer",
                {}
            ),

        "fallback":
            decision.get(
                "fallback",
                False
            ),

        "status":
            "REPORT_READY"

    }
