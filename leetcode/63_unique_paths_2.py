"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. 
A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example 1:
    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right

Example 2:
    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1
"""

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = {}

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i,j)==(m-1,n-1): # first iteration
                    dp[(i,j)] = 1-obstacleGrid[i][j]
                    continue
                
                if obstacleGrid[i][j] == 0:
                    dp[(i,j)] = dp.get((i+1,j), 0) + dp.get((i, j+1), 0)
                else:
                    dp[(i,j)] = 0

        return dp[(0, 0)]