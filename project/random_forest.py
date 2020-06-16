from sklearn.ensemble import RandomForestClassifier


# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
class RandomForestWrapper:
    def __init__(self):
        print('Random Forest')
        self.classifier = RandomForestClassifier(n_estimators=50, n_jobs=8)

    def fit_and_calculate_score(self, X, y, val_X, val_y):
        print('Fitting to given X')
        self.classifier = self.classifier.fit(X, y)
        print('Calculating score on test set')
        return self.classifier.score(val_X, val_y)

