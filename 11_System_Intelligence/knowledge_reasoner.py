
class KnowledgeReasoner:


    def analyze(self, knowledge):

        result = {

            "strength":
                knowledge.get(
                    "strength",
                    0
                ),

            "trend":
                knowledge.get(
                    "trend",
                    "unknown"
                ),

            "reasoning":
                "knowledge analyzed"

        }

        return result
