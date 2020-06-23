from classification_wrapper import ClassificationWrapper
from sklearn.neighbors import (NeighborhoodComponentsAnalysis,
KNeighborsClassifier)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


class KNearestNeighborsWrapper(ClassificationWrapper):
    def __init__(self):
        nca = NeighborhoodComponentsAnalysis(random_state=42)
        knn = KNeighborsClassifier(n_neighbors=5)
        self.classifier = Pipeline([('nca', nca), ('knn', knn)])

