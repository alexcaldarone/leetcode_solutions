"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

Example 2:
    Input: nums = [2,0,1]
    Output: [0,1,2]
"""

from collections import defaultdict
from typing import List 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return nums

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        colors = [0, 1, 2]

        prev_stop = 0
        for color in colors:
            freq = counts.get(color, 0)
            for i in range(freq):
                nums[i+prev_stop] = color
            prev_stop += freq