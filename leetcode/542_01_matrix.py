"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

Example 1:
    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
    Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        def valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS
        
        ROWS = len(mat)
        COLS = len(mat[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = [[0] * COLS for _ in range(ROWS)]
        queue = deque()
        seen = set()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    seen.add((r, c))
        
        while queue:
            x, y, dist = queue.popleft()

            for dx, dy in dirs:
                if valid(x+dx, y+dy) and (x+dx, y+dy) not in seen:
                    queue.append((x+dx, y+dy, dist+1))
                    seen.add((x+dx, y+dy))
                    res[x+dx][y+dy] = dist+1
        
        return res