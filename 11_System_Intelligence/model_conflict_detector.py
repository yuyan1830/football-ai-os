
class ModelConflictDetector:


    def detect(self,models):

        values=list(models.values())

        return {

            "conflict":
                max(values)-min(values)>0.4

        }
