# -*- coding: utf-8 -*-

"""
Football AI OS
AI Runtime Adapter V1.0

Purpose:

Connect API Layer with AI_RUNTIME.

Responsibility:

API request
        |
        
Format conversion
        |
        
AI_RUNTIME execution
        |
        
Return result

This module does not:
- calculate models
- access database
- modify model parameters
"""


from AI_RUNTIME.engine import execute



def run_ai_runtime(match):

    """
    Receive API format:

    {
        "home":"Manchester City",
        "away":"Liverpool"
    }

    Convert to AI_RUNTIME format:

    MATCH_ANALYSIS:home:away
    """


    home = match.get(
        "home",
        ""
    )

    away = match.get(
        "away",
        ""
    )


    if not home or not away:

        return {

            "status":
            "INVALID_MATCH_PARAMETER"

        }



    message = (
        "MATCH_ANALYSIS:"
        + home
        + ":"
        + away
    )


    result = execute(
        "MATCH_ANALYSIS",
        message
    )


    return result
