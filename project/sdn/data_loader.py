import pandas as pd
from sklearn import preprocessing
import seaborn as sn
from matplotlib import pyplot


class CustomSDNReader:

    def _get_df(self, path):
        df = pd.read_csv(path, delimiter=',', header=None)
        new_header = df.iloc[0]  # grab the first row for the header
        df = df[1:]  # take the data less the header row
        df.columns = new_header  # set the header row as the df header
        return df

    def read(self, train_size=1000):

        print('--------------------------------------------------------')
        print('--------------------------------------------------------')
        print(f'-------------------Train Size {train_size}-----------------------')
        print('--------------------------------------------------------')
        print('--------------------------------------------------------')

        df = self._get_df(f'sdn/sdn_datasets/train/train.{train_size}.csv')
        self.dataset_stats(df)

        X_train, y_train, y_label_mapping = self.numerize(df)
        df = self._get_df(f'sdn/sdn_datasets/validation/val.100.csv')
        X_val, y_val, _ = self.numerize(df, y_label_mapping)
        df = self._get_df(f'sdn/sdn_datasets/test/test.10000.csv')
        X_test, y_test, _ = self.numerize(df, y_label_mapping)

        return {
            'train':
                {'X': X_train, 'y': y_train},
            'validation':
                {'X': X_val, 'y': y_val},
            'test':
                {'X': X_test, 'y': y_test},
            'y_encoding': y_label_mapping
        }

    def numerize(self, df, label_encoding=None):
        y = df[df.columns[-1]]
        X = df[df.columns[:-1]]

        if not label_encoding:
            le = preprocessing.LabelEncoder()
            y = le.fit_transform(y)
            label_mapping = {t[1]: t[0] for t in enumerate(le.classes_)}

            return X.astype('float64'), y, label_mapping
        else: # Keep the same mapping for this set too
            for str_form, mapped_int in label_encoding.items():
                y = y.replace(str_form, mapped_int)
            return X.astype('float64'), y, label_encoding

    def normalize(self, df):
        x = df.values  #returns a numpy array
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x)
        return pd.DataFrame(x_scaled, columns=df.columns)

    def scale(self, df):
        return pd.DataFrame(preprocessing.scale(df), columns=df.columns)

    def dataset_stats(self, df):
        # Statistical summary of dataset
        print("Statistical summary of the dataset:")
        print(df.describe())
        print("--------------------------------------------------------")

        # X, _, _ = self.numerize(df)
        # print(X)
        # # Correlation between variables
        # sn.heatmap(X.corr(), annot=True)
        # pyplot.show()
        # # Histogram of value distribution
        # X.hist()
        # pyplot.show()
