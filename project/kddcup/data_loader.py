import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


class KddcupDataReader:

    @staticmethod
    def read():
        string_fields = [1, 2, 3]

        df = pd.read_csv('kddcup/kddcup_10_percent.csv', delimiter=',',  header=None)

        y = df[df.columns[-1]]
        le = preprocessing.LabelEncoder()
        y = le.fit_transform(y)
        label_mapping = {t[1]: t[0] for t in enumerate(le.classes_)}

        for string_field_idx in string_fields:
            c = df[df.columns[string_field_idx]]
            le = preprocessing.LabelEncoder()
            c = le.fit_transform(c)
            df[df.columns[string_field_idx]] = c
            label_mapping = {t[1]: t[0] for t in enumerate(le.classes_)}
        X = df[df.columns[:-1]]

        return X, y, label_mapping

    @staticmethod
    def train_test_split(X, y, test_size=0.33, random_state=42):
        return train_test_split(X, y, test_size, random_state)
