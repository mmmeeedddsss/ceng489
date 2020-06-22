from sklearn.tree import DecisionTreeClassifier
from classification_wrapper import ClassificationWrapper


# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
class DecisionTreeWrapper(ClassificationWrapper):
    """for more information about trees: https://scikit-learn.org/stable/modules/tree.html"""
    def __init__(self):
        print("Decision Tree")
        self.classifier = DecisionTreeClassifier()
