
class PerformanceTracker:


    def __init__(self):

        self.history=[]


    def add(self,score):

        self.history.append(score)


    def average(self):

        if not self.history:
            return 0

        return round(
            sum(self.history)/len(self.history),
            4
        )
