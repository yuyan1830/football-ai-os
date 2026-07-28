def final_decision(fusion):

    probs={
        "主胜":fusion["home_win_probability"],
        "平局":fusion["draw_probability"],
        "客胜":fusion["away_win_probability"]
    }

    result=max(probs,key=probs.get)

    confidence=max(probs.values())

    if confidence>=0.55:
        risk="LOW"
    elif confidence>=0.45:
        risk="MEDIUM"
    else:
        risk="HIGH"

    return {
        "decision":result,
        "confidence":round(confidence,4),
        "risk_level":risk,
        "probabilities":probs,
        "status":"DECISION_COMPLETED"
    }
