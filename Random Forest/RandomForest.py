import numpy as np
from DecisionTree import DecisionTree
from collections import Counter

class RandomForest:

    def __init__(self, n_trees=100, min_samples_split=2, max_depth=100, n_features=None):
        self.n_trees = n_trees
        self.min_samples_split=min_samples_split
        self.max_depth=max_depth
        self.n_features=n_features
        self.trees = []

    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_trees):
            tree = DecisionTree(min_samples_split=self.min_samples_split,
                                max_depth=self.max_depth,
                                n_features=self.n_features)
            X_sample, y_sample = self._bootstrap_sample(X, y)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)

    def _bootstrap_sample(self, X, y):
        n_samples = X.shape[0]
        idxs = np.random.choice(n_samples, n_samples, replace=True)
        return X[idxs], y[idxs]

    def _most_common_label(self, y):
        counter = Counter(y)
        value = counter.most_common(1)[0][0]
        return value


    def predict(self, x):
        predictions = np.array([tree.predict(x) for tree in self.trees])
        #[[1,0,1,1],[0,0,1,1],[1,1,1,1]]
        #[[1,0,1]]
        tree_preds = np.swapaxes(predictions,0,1)
        predictions = np.array([self._most_common_label(tree_pred) for tree_pred in tree_preds])
        return predictions