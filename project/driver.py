import operator
from sdn.data_loader import CustomSDNReader
from random_forest import RandomForestWrapper
from sklearn.metrics import classification_report

data = CustomSDNReader.read(train_size=1000)

pred_y = RandomForestWrapper().fit_and_calculate_score(data['train']['X'],
                                                       data['train']['y'],
                                                       data['test']['X'])

sorted_labels = sorted(data['y_encoding'].items(), key=operator.itemgetter(1))
sorted_labels = [label[0] for label in sorted_labels]
print(classification_report(data['test']['y'], pred_y, target_names=sorted_labels, digits=3))
