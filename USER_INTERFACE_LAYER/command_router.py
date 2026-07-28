
def route(command):

    if "analysis" in command or "分析" in command:
        return "MATCH_ANALYSIS"

    if "model" in command or "模型" in command:
        return "MODEL_STATUS"

    if "backtest" in command or "回测" in command:
        return "BACKTEST"

    return "GENERAL_QUERY"
