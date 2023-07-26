import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from RandomForest import RandomForest

bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

clf = RandomForest()
clf.fit(X_train,y_train)
predictions = clf.predict(X_test)

def accuracy(y_true, y_pred):
    return np.sum(y_true ==y_pred)/len(y_true)

acc = accuracy(y_test, predictions)
print(acc)