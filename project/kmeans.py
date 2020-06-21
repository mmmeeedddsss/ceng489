from sklearn.cluster import KMeans
from classification_wrapper import ClassificationWrapper


# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
class KMeansWrapper(ClassificationWrapper):
    def __init__(self):
        print('Gaussian Naive Bayes')
        self.classifier = KMeans(n_clusters=6)

    def fit_and_calculate_score(self, X, y, test_X):
        print('Fitting to given X')
        self.classifier = self.classifier.fit(X)
        return self.classifier.predict(test_X)
