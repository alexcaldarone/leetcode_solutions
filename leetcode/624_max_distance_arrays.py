"""
You are given m arrays, where each array is sorted in ascending order.
You can pick up two integers from two different arrays (each array picks one) and calculate the distance. 
We define the distance between two integers a and b to be their absolute difference |a - b|.
Return the maximum distance.

Example 1:
    Input: arrays = [[1,2,3],[4,5],[1,2,3]]
    Output: 4
    Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Example 2:
    Input: arrays = [[1],[1]]
    Output: 0
"""

from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins = [min(arr) for arr in arrays]
        maxs = [max(arr) for arr in arrays]
        
        best_max = [float("-inf"), 0]
        for i, n in enumerate(maxs):
            if n > best_max[0]:
                best_max = [n,i]
        second_best_max = [float("-inf"), 0]
        for i,n in enumerate(maxs):
            if n >= second_best_max[0] and n <= best_max[0] and i != best_max[1]:
                second_best_max = [n, i]
        if second_best_max[0] == float("-inf"):
            second_best_max[0] = best_max[0]
        
        best = float("-inf")
        for j in range(len(mins)):
            curr_min = mins[j]
            #valid_maxs = maxs[:i] + maxs[i+1:]
            if best_max[1] == j:
                if abs(second_best_max[0] - curr_min) > best:
                    best = abs(second_best_max[0] - curr_min)
            else:
                if abs(best_max[0] - curr_min) > best:
                    best = abs(best_max[0] - curr_min)

        return best