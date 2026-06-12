"""
You are given an undirected weighted graph of n nodes (0-indexed), 
represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability 
of success of traversing that edge succProb[i].
Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return 
its success probability.
If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:
    Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
    Output: 0.25000
    Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
    Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
    Output: 0.30000

Example 3:
    Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
    Output: 0.00000
    Explanation: There is no path between 0 and 2.
"""

import heapq
from collections import defaultdict
import math
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for idx, (i, j) in enumerate(edges):
            adj[i].append((j, succProb[idx]))
            adj[j].append((i, succProb[idx]))
        
        path_probs = [float("-inf") for _ in range(n)]
        path_probs[start_node] = 0
        q = [(0, start_node)]
        heapq.heapify(q)
        while q:
            log_prob, node = heapq.heappop(q)
            log_prob *= -1
            for neig, neig_prob in adj[node]:
                if neig_prob > 0 and log_prob + math.log(neig_prob) > path_probs[neig]:
                    path_probs[neig] = log_prob + math.log(neig_prob)
                    heapq.heappush(q, (-path_probs[neig], neig))

        if path_probs[end_node] == float("inf"):
            return 0
        else:
            return math.exp(path_probs[end_node])