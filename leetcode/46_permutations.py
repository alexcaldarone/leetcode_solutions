"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        res = []

        def backtrack(curr, used):
            nonlocal res
            nonlocal nums
            if len(curr) == len(nums):
                res.append(curr)
                return
            
            for i, num in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    backtrack(curr + [num], used)
                    used[i] = False
            
        backtrack([], used)
        return res