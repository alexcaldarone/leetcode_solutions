"""
Implemnentation of Classification and Regression Trees (CART) algorithm.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Tuple

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
    pass

class ClassificationTree(DecisionTree):
    pass

class RegressionTree(DecisionTree):
    pass
