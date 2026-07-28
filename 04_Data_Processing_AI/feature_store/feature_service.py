class FeatureService:

    def load_features(self):
        return {
            "status":"ready",
            "service":"feature_service"
        }


if __name__=="__main__":
    print(FeatureService().load_features())
