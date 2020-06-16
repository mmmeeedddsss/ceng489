import pandas as pd
from sklearn import preprocessing


class CustomSDNReader:

    @staticmethod
    def _get_df(path):
        df = pd.read_csv(path, delimiter=',', header=None)
        new_header = df.iloc[0]  # grab the first row for the header
        df = df[1:]  # take the data less the header row
        df.columns = new_header  # set the header row as the df header
        return df

    @staticmethod
    def read(train_size=100):
        string_fields = [1, 2, 3]

        print('Training Data loading stared')
        df = CustomSDNReader._get_df(f'sdn/sdn_datasets/train/train.{train_size}.csv')
        print('Training Data loading has done!')

        X_train, y_train, y_label_mapping = CustomSDNReader.numerize(df)

        print('Validation Data loading stared')
        df = CustomSDNReader._get_df(f'sdn/sdn_datasets/validation/val.100.csv')
        print('Validation Data loading has done!')

        X_val, y_val, _ = CustomSDNReader.numerize(df, y_label_mapping)

        print('Test Data loading stared')
        df = CustomSDNReader._get_df(f'sdn/sdn_datasets/test/test.10000.csv')
        print('Test Data loading has done!')

        X_test, y_test, _ = CustomSDNReader.numerize(df, y_label_mapping)

        return {
            'train':
                {'X': X_train, 'y': y_train},
            'validation':
                {'X': X_val, 'y': y_val},
            'test':
                {'X': X_val, 'y': y_val},
            'y_encoding': y_label_mapping
        }

    @staticmethod
    def numerize(df, label_encoding=None):
        y = df[df.columns[-1]]
        X = df[df.columns[:-1]]

        print('Converting Strings to Ints')
        if not label_encoding:  # Keep the same mapping for this set too
            le = preprocessing.LabelEncoder()
            y = le.fit_transform(y)
            label_mapping = {t[1]: t[0] for t in enumerate(le.classes_)}
            print('Label mapping is done as :', label_mapping)
            print(y)

            return X, y, label_mapping
        else:
            for str_form, mapped_int in label_encoding.items():
                y = y.replace(str_form, mapped_int)
            return X, y, label_encoding
