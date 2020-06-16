from sklearn.ensemble import RandomForestClassifier


# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
class RandomForestWrapper:
    def __init__(self):
        print('Random Forest')
        self.classifier = RandomForestClassifier(n_estimators=50, n_jobs=8)

    def fit_and_calculate_score(self, X, y, test_X):
        print('Fitting to given X')
        self.classifier = self.classifier.fit(X, y)
        return self.classifier.predict(test_X)

