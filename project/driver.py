import operator
from sdn.data_loader import CustomSDNReader
from random_forest import RandomForestWrapper
from gaussian_naive_bayes import GaussianNBWrapper
from sklearn.metrics import classification_report
from nearest_centroid import NearestCentroidWrapper
from kmeans import KMeansWrapper

def read_train_and_test(classifier=RandomForestWrapper):
    for train_size in [100, 200, 400, 800, 1000]:
        data = CustomSDNReader.read(train_size=train_size)

        pred_y = classifier().fit_and_calculate_score(data['train']['X'],
                                                            data['train']['y'],
                                                            data['test']['X'])

        sorted_labels = sorted(data['y_encoding'].items(), key=operator.itemgetter(1))
        sorted_labels = [label[0] for label in sorted_labels]
        print(classification_report(data['test']['y'], pred_y, target_names=sorted_labels, digits=3))


if __name__ == '__main__':
    read_train_and_test(KMeansWrapper)
