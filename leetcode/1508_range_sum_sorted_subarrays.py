"""
You are given the array nums consisting of n positive integers. 
You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, 
creating a new array of n * (n + 1) / 2 numbers.
Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. 
Since the answer can be a huge number return it modulo 109 + 7.

Example 1:
    Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
    Output: 13 
    Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. 
        After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. 
        The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 

Example 2:
    Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
    Output: 6
    Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. 
        The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.

Example 3:
    Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
    Output: 50
"""

from typing import List
import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        # computing subarray sums
        for l in range(0, len(nums)):
            for r in range(l+1, len(nums)+1):
                #print(nums[l:r])
                sums.append(sum(nums[l:r]))
        
        sums.sort()
        return sum(sums[left-1:right]) % (10**9 + 7)

# using priority queue, not actually faster
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        import heapq
        sums = []
        heapq.heapify(sums)
        # computing subarray sums
        for l in range(0, len(nums)):
            for r in range(l+1, len(nums)+1):
                heapq.heappush(sums, sum(nums[l:r]))
        
        i = 0
        res = 0
        while i < left-1:
            heapq.heappop(sums)
            i += 1
        while left-1 <= i < right:
            res += heapq.heappop(sums)
            i += 1
        return res % (10**9 + 7)

# smarter priority queue solution
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(l)

        res = 0
        for j in range(1, right+1):
            x, i = heapq.heappop(l)
            if j >= left:
                res += x
            if i+1 < len(nums):
                heapq.heappush(l, (x + nums[i+1], i+1))
        
        return res % (10**9 + 7)