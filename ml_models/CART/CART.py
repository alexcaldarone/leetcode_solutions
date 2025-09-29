"""
Implemnentation of Classification and Regression Trees (CART) algorithm.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
)

# D is a matrix that has as last column the labels

class Node(object):
    """
    Represents a node in the decision tree.
    """
    def __init__(self) -> None:
        self.__left = None
        self.__right = None
        self.__split = None
        self.value = None
        self.__feature = None

    def set_params(self, split: float, feature: int) -> None:
        self.__split = split
        self.__feature = feature

    def get_params(self) -> Tuple[float, int]:
        return self.__split, self.__feature
    
    def set_children(self, left: Node, right: Node) -> None:
        self.__left = left
        self.__right = right
    
    def get_left(self) -> Optional[Node]:
        return self.__left

    def get_right(self) -> Optional[Node]:
        return self.__right

class DecisionTree(ABC):
    """
    Abstract base class for decision trees.
    """
    def __init__(self, max_depth: int = None, min_samples_split: int = 2) -> None:
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None
    
    @abstractmethod
    def _impurity(self, D: np.ndarray) -> None:
        pass

    @abstractmethod
    def _leaf_value(self, D: np.ndarray) -> None:
        pass

    def __candidate_thresholds(self, feature: np.ndarray) -> np.ndarray:
        vals = np.asarray(feature, dtype=float)
        uniq = np.unique(vals)
        if uniq.size < 2:
            return np.array([], dtype=float)
        # midpoints between consecutive unique values
        mids = (uniq[:-1] + uniq[1:]) / 2.0
        return mids

    def __grow(self, node: Node, D: np.ndarray, level: int) -> None:
        if D is not None and D.shape[0] != 0:
            max_depth = (self.max_depth is None) or (level < self.max_depth)
            min_sample = self.min_samples_split <= D.shape[0]
            n_classes = np.unique(D[:, -1]).shape[0] > 1

            # if a leaf node
            if not (max_depth and min_sample and n_classes):
                node.value = self._leaf_value(D)
                return
            best_node_impurity = None
            best_feature = None
            best_split = None
            best_left = None
            best_right = None

            for feat in range(D.shape[-1]-1):
                thresholds = self.__candidate_thresholds(D[:, feat])
                if thresholds.size == 0:
                    continue
                for sp_idx, spl in enumerate(thresholds):
                    left_data = D[D[:, feat] <= spl]
                    right_data = D[D[:, feat] > spl]

                    # if non empty
                    if left_data.size and right_data.size:
                        N = D.shape[0]
                        N_left = left_data.shape[0]
                        N_right = right_data.shape[0]

                        impurity = (N_left / N)*self._impurity(left_data) + (N_right / N)*self._impurity(right_data)

                        if best_node_impurity is None or impurity < best_node_impurity:
                            best_node_impurity = impurity
                            best_feature = feat
                            best_split = spl
                            best_left = left_data
                            best_right = right_data
            
            if best_node_impurity is None:
                node.value = self._leaf_value(D)
                return
            
            node.set_params(best_split, best_feature)
            left_node = Node()
            right_node = Node()
            node.set_children(left_node, right_node)
            self.__grow(left_node, best_left, level+1)
            self.__grow(right_node, best_right, level+1)
        else:
            return

    def __traverse(self, node: Node, x: np.ndarray) -> float:
        """
        Traverse the tree to make a prediction for a single sample.
        """
        if node.get_left() is None and node.get_right() is None:
            return node.value
        
        split, feature = node.get_params()
        if feature is None or split is None:
            return node.value
        
        if x[feature] <= split:
            return self.__traverse(node.get_left(), x)
        else:
            return self.__traverse(node.get_right(), x)

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        D = np.concatenate((X, y.reshape(-1, 1)), axis=1)
        self.root = Node()
        self.__grow(self.root, D, 1)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict the labels for a set of samples.
        """
        return np.array([self.__traverse(self.root, x) for x in X])

class ClassificationTree(DecisionTree):
    def __init__(self, max_depth: int = None, min_samples_split: int = 2, loss: str = "gini") -> None:
        super().__init__(max_depth, min_samples_split)
        self.loss = loss

    def __gini(self, D: np.ndarray) -> float:
        y = D[:, -1]
        _, counts = np.unique(y, return_counts=True)
        impurity = 0
        total = len(y)
        for count in counts:
            prob = count / total
            impurity += prob*(1 - prob)
        return impurity

    def __entropy(self, D: np.ndarray) -> float:
        y = D[:, -1]
        _, counts = np.unique(y, return_counts=True)
        total = len(y)
        probs = counts / total
        return -np.sum(probs * np.log2(probs + 1e-9))

    def _impurity(self, D: np.ndarray) -> float:
        if self.loss == "gini":
            return self.__gini(D)
        elif self.loss == "entropy":
            return self.__entropy(D)
        else:
            raise ValueError("Invalid loss function")

    def _leaf_value(self, D: np.ndarray) -> float:  
        y = D[:, -1]
        values, counts = np.unique(y, return_counts=True)
        return values[np.argmax(counts)]

class RegressionTree(DecisionTree):
    def __init__(
            self, 
            max_depth: int = None, 
            min_samples_split: int = 2, 
            loss: str = "mse"
        ) -> None:
        super().__init__(max_depth, min_samples_split)
        self.loss = loss

    def __mse(self, D: np.ndarray) -> float:
        y = D[:, -1]
        y_hat = np.mean(y)
        return mean_squared_error(y, [y_hat]*len(y))

    def __mae(self, D: np.ndarray) -> float:
        y = D[:, -1]
        y_hat = np.mean(y)
        return mean_absolute_error(y, [y_hat]*len(y))

    def _impurity(self, D: np.ndarray) -> float:
        if self.loss == "mse":
            return self.__mse(D)
        elif self.loss == "mae":
            return self.__mae(D)
        else:
            raise ValueError("Invalid loss function")

    def _leaf_value(self, D: np.ndarray) -> float:  
        y = D[:, -1]
        return np.mean(y)