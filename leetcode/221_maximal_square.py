"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 4

Example 2:
    Input: matrix = [["0","1"],["1","0"]]
    Output: 1

Example 3:
    Input: matrix = [["0"]]
    Output: 0
"""

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        best = 0

        for i in range(m):
            best = max(best, int(matrix[i][0]))
        for j in range(n):
            best = max(best, int(matrix[0][j]))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    matrix[i][j] = 1 + min(
                        int(matrix[i-1][j]),
                        int(matrix[i-1][j-1]),
                        int(matrix[i][j-1])
                    )

                    best = max(best, int(matrix[i][j]))
        
        return best**2