

class ClassificationWrapper:
    """Base class for wrapper of classification models"""

    def fit_and_calculate_score(self, X, y, test_X):
        print('Fitting to given X')
        self.classifier = self.classifier.fit(X, y)
        return self.classifier.predict(test_X)

