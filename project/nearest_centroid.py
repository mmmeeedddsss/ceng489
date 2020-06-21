from sklearn.neighbors import NearestCentroid
from classification_wrapper import ClassificationWrapper


class NearestCentroidWrapper(ClassificationWrapper):
    """https://scikit-learn.org/stable/modules/neighbors.html#nearest-centroid-classifier"""
    def __init__(self):
        print('Nearest Centroid Classifier')
        self.classifier = NearestCentroid()
