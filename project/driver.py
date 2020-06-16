from sdn.data_loader import CustomSDNReader

from random_forest import RandomForestWrapper

data = CustomSDNReader.read(train_size=1000)

print('Random forest with n labels accuracy',
      RandomForestWrapper().fit_and_calculate_score(data['train']['X'],
                                                    data['train']['y'],
                                                    data['validation']['X'],
                                                    data['validation']['y']))


