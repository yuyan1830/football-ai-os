def route(command):

    if "分析" in command or "预测" in command or "MATCH_ANALYSIS" in command:
        return "MATCH_ANALYSIS"

    if "模型" in command or "MODEL" in command:
        return "MODEL_STATUS"

    if "回测" in command or "BACKTEST" in command:
        return "BACKTEST"

    return "GENERAL_QUERY"
