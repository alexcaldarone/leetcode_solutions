"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        spiral = []

        while l < r and top < bottom:
            
            for i in range(l, r):
                spiral.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom):
                spiral.append(matrix[i][r-1])
            r -= 1
            
            # check if we are at the end
            if l >= r or top >= bottom:
                break

            for i in range(r-1, l-1, -1):
                spiral.append(matrix[bottom-1][i])
            bottom -= 1
            
            for i in range(bottom-1, top-1, -1):
                spiral.append(matrix[i][l])
            l += 1
        
        return spiral