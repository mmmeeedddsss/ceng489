from sklearn.naive_bayes import GaussianNB
from classification_wrapper import ClassificationWrapper


# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
class GaussianNBWrapper(ClassificationWrapper):
    def __init__(self):
        print('Gaussian Naive Bayes')
        self.classifier = GaussianNB()
