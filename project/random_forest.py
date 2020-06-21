from sklearn.ensemble import RandomForestClassifier
from classification_wrapper import ClassificationWrapper


# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
class RandomForestWrapper(ClassificationWrapper):
    def __init__(self):
        print('Random Forest')
        self.classifier = RandomForestClassifier(n_estimators=50, n_jobs=8)
