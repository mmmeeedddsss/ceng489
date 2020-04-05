import numpy as np
import pandas as pd
from sklearn import preprocessing


class KddcupDataReader:

    @staticmethod
    def read():
        string_fields = [1, 2, 3]

        print('Data loading stared')
        df = pd.read_csv('kddcup/kddcup_10_percent.csv', delimiter=',',  header=None)
        print('Data loading has done!')

        y = df[df.columns[-1]]
        print('Converting Strings to Ints')
        le = preprocessing.LabelEncoder()
        y = le.fit_transform(y)
        label_mapping = {t[1]: t[0] for t in enumerate(le.classes_)}
        print('Label mapping is done as :', label_mapping)
        print(y)

        for string_field_idx in string_fields:
            c = df[df.columns[string_field_idx]]
            le = preprocessing.LabelEncoder()
            c = le.fit_transform(c)
            df[df.columns[string_field_idx]] = c
            label_mapping = {t[1]: t[0] for t in enumerate(le.classes_)}
            print('Mapping of column {} has done as :'.format(string_field_idx), label_mapping)
        print('Done')
        X = df[df.columns[:-1]]

        return X, y, label_mapping

