"""
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Note that the product of an array with a single element is the value of that element.

Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max, curr_min, res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            temp = max(curr, max(curr*curr_max, curr*curr_min))
            curr_min = min(curr, min(curr*curr_max, curr*curr_min))
            curr_max = temp
            res = max(res, curr_max)
        
        return res