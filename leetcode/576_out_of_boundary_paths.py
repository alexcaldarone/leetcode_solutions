"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. 
You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. 
Since the answer can be very large, return it modulo 10^9 + 7.

Example 1:
    Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
    Output: 6

Example 2:
    Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
    Output: 12
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = {}

        def dfs(i, j, num_move):
            nonlocal m
            nonlocal n
            nonlocal maxMove
            # base case
            if i >= m or j >= n or i < 0 or j < 0:
                return 1
            
            if (i, j, num_move) in dp:
                return dp[(i, j, num_move)]
            
            total = 0
            if num_move < maxMove:
                for move_r, move_c in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    total += dfs(i+move_r, j+move_c, num_move+1)
            dp[(i, j, num_move)] = total
            return total

        return dfs(startRow, startColumn, 0) % MOD
