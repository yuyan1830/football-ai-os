
"""
Optimization Suggestion Compatibility Layer
"""


from optimization_suggestion_engine import OptimizationSuggestionEngine


class OptimizationSuggestion:

    def __init__(self):

        self.engine = OptimizationSuggestionEngine()


    def generate(self):

        return {
            "status":"ready"
        }
