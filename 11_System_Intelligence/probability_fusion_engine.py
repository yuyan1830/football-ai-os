
class ProbabilityFusionEngine:

    def fuse(self, models):

        total = sum(models.values())

        if total == 0:
            return {
                "home":0,
                "draw":0,
                "away":0
            }

        return {

            "home":
                round(models.get("elo",0)/total,4),

            "draw":
                round(models.get("poisson",0)/total,4),

            "away":
                round(models.get("xgboost",0)/total,4)

        }
