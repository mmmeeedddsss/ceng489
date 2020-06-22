from sklearn.svm import SVC
from classification_wrapper import ClassificationWrapper


# https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
class SVCWrapper(ClassificationWrapper):
    """for multiclass classification with SVM's see
    https://scikit-learn.org/stable/modules/svm.html#multi-class-classification """
    def __init__(self):
        print("SVC")
        self.classifier = SVC()
