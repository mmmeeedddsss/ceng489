from kddcup.data_loader import KddcupDataReader
from sklearn.model_selection import train_test_split

from random_forest import RandomForestWrapper

X, y, label_mapping = KddcupDataReader.read()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# 0.9997055702429659  ???
print('Random forest with n labels accuracy',
      RandomForestWrapper().fit_and_calculate_score(X_train, y_train, X_test, y_test))
