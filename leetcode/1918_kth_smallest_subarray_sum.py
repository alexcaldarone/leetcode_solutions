"""
Given an integer array nums of length n and an integer k, return the kth smallest subarray sum.
A subarray is defined as a non-empty contiguous sequence of elements in an array. A subarray sum is the sum of all elements in the subarray.

Example 1:
    Input: nums = [2,1,3], k = 4
    Output: 3
    Explanation: The subarrays of [2,1,3] are:
    - [2] with sum 2
    - [1] with sum 1
    - [3] with sum 3
    - [2,1] with sum 3
    - [1,3] with sum 4
    - [2,1,3] with sum 6 
    Ordering the sums from smallest to largest gives 1, 2, 3, 3, 4, 6. The 4th smallest is 3.

Example 2:
    Input: nums = [3,3,5,5], k = 7
    Output: 10
    Explanation: The subarrays of [3,3,5,5] are:
    - [3] with sum 3
    - [3] with sum 3
    - [5] with sum 5
    - [5] with sum 5
    - [3,3] with sum 6
    - [3,5] with sum 8
    - [5,5] with sum 10
    - [3,3,5], with sum 11
    - [3,5,5] with sum 13
    - [3,3,5,5] with sum 16
    Ordering the sums from smallest to largest gives 3, 3, 5, 5, 6, 8, 10, 11, 13, 16. The 7th smallest is 10.
"""

from typing import List

# works but is slow
class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        import heapq
        sums = []
        
        heapq.heapify(sums)
        n = len(nums)

        for length in range(1, n+1):
            for i in range(0, n-length+1):
                heapq.heappush(sums, -sum(nums[i:i+length]))

                while len(sums) > k:
                    heapq.heappop(sums)
        return -sums[0]

# efficient solution using binary search
class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def _count_less(x, nums):
            l = 0
            curr_sum = 0
            count = 0
            n = len(nums)
            for r in range(n):
                curr_sum += nums[r]
                while curr_sum > x:
                    curr_sum -= nums[l]
                    l += 1
                count += (r-l+1)
            return count
        
        l, r = 0, sum(nums)

        while l < r:
            mid = (l+r)//2
            cnt = _count_less(mid, nums)

            if cnt >= k:
                r = mid
            else:
                l = mid + 1
        
        return l