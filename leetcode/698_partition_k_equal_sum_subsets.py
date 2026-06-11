"""
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
    Input: nums = [4,3,2,3,5,2,1], k = 4
    Output: true
    Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
    Input: nums = [1,2,3,4], k = 3
    Output: false
"""

from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool: 
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k

        if max(nums) > target:
            return False

        used = [False] * len(nums)
        nums.sort(reverse=True)

        def backtrack(bucket_num, curr, idx):
            # base case
            nonlocal target
            nonlocal k
            nonlocal used
            if bucket_num == k-1:
                return True

            if curr == target:
                return backtrack(bucket_num + 1, 0, 0)
            
            for i in range(idx, len(nums)):
                if not used[i] and curr + nums[i] <= target:
                    used[i] = True
                    if backtrack(bucket_num, curr + nums[i], i+1):
                        return True
                    used[i] = False
            
            return False
        
        return backtrack(0, 0, 0)