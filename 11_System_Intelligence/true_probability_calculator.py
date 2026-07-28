
class TrueProbabilityCalculator:


    def calculate(self,data):

        return {

            "home_probability":
                data.get("home",0),

            "draw_probability":
                data.get("draw",0),

            "away_probability":
                data.get("away",0)

        }
