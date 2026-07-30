def route(command):


    if "分析" in command or "analysis" in command:
        return "MATCH_ANALYSIS"


    if "模型" in command or "model" in command:
        return "MODEL_STATUS"


    if "回测" in command or "backtest" in command:
        return "BACKTEST"


    return "GENERAL_QUERY"

