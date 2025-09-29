from typing import List
import math

"""
Studying for ML internships.

Implementation of ML algorithms from scratch.

Implement a classification algorithm from scratch using only the standard library
"""

# I choos to implement the KNN algorithm from scratch
# What is kNN? Describe it.

class kNNClassifier:
    def __init__(self, x: List[List[float]], y: List[str]):
        self.x = x
        self.y = y
    
    def classify(self, new_point: List[float], k: int):
        # this is a function that, given a new point
        # classifies it
        # for now we consider the euclidean distance
        # though this could be extended to use any other distance function (how?)
        distances = [(i, sum((new_point[j] - self.x[i][j])**2 for j in range(len(new_point)))) for i in range(len(self.x))]
        distances = [(dist[0], math.sqrt(dist[1])) for dist in distances] # square root to get euclidean distance

        # once we have distances, we have to find the k smallest elements of the array
        distances.sort(key = lambda x: x[1])
        # returns the sorted distances, where the elements are ordered in increasing manner
        
        # find the indices of the closest points
        min_idx = []
        for i in range(k):
            min_idx.append(distances[i][0])
        
        # return the most popular class in these indices
        candidate_y = [y[i] for i in min_idx]

        # find the most frequent element in candidate_y
        estimate_idx = float("-inf")
        counts = {}
        for i, el in enumerate(candidate_y):
            counts[el] = 1 + counts.get(el, 0)
            if counts[el] > estimate_idx:
                estimate_idx = i
        
        return y[estimate_idx]


if __name__ == "__main__":
    X = [[1, 0], [0, 0], [0, 1], [-1, -1], [-0.6, -0.6]]
    y = ["a", "a", "b", "b", "a"]

    classifier = kNNClassifier(X, y)
    print(classifier.classify([-0.5, -0.5], k = 2))