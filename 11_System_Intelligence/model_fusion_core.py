
class ModelFusionCore:


    def fuse(self,models):

        total=sum(models)

        return {

            "fusion_probability":
                round(
                    total/len(models),
                    4
                )

        }
