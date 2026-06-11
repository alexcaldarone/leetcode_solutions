"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum 
of the elements in both subsets is equal or false otherwise.

Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
    Input: nums = [1,2,3,5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        dp = [0] * (target+1)

        for j in range(len(nums)):
            w = nums[j]
            for i in range(target, w-1, -1):
                dp[i] = max(dp[i], dp[i-w] + w)
            
        return dp[-1] == target