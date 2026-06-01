"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).

Example 1:
    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
    Input: matrix = [[-5]], k = 1
    Output: -5
"""

from typing import List

# trivial solution O(n^2) time and memory
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                res.append(matrix[i][j])
        
        res.sort()
        return res[k-1]

# smarter solution with heap
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        res = []
        heapq.heapify(res)
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                heapq.heappush(res, -matrix[i][j])

                while len(res) > k:
                    heapq.heappop(res)
        
        return - heapq.heappop(res)

# binary search
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        def _count_less_than(matrix, mid):
            # counts the number of values less than mid
            n = len(matrix)
            row, col = n-1, 0
            cnt = 0

            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    cnt += row+1
                    col += 1
                else:
                    row -= 1
            return cnt
        
        n = len(matrix)
        l = matrix[0][0]
        r = matrix[n-1][n-1]

        while l < r:
            mid = l + (r-l)/2
            if _count_less_than(matrix, mid) < k:
                l = mid + 1
            else:
                r = mid
        
        return int(l)