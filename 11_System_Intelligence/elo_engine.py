
class EloEngine:


    def calculate(self, home, away):

        diff = home-away

        probability = 1/(1+10**(-diff/400))

        return {

            "home_win":
                round(probability,4),

            "away_win":
                round(1-probability,4)

        }
