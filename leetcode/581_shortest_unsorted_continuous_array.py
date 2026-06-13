"""
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, 
then the whole array will be sorted in non-decreasing order.
Return the shortest such subarray and output its length.

Example 1:
    Input: nums = [2,6,4,8,10,9,15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
    Input: nums = [1,2,3,4]
    Output: 0

Example 3:
    Input: nums = [1]
    Output: 0
"""

from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        moved_l, moved_r = False, False
        start, end = 0, len(nums)-1
        for l in range(0, len(nums)-1):
            if nums[l+1] < nums[l]:
                moved_l = True
                start = l
                break
        
        for r in range(len(nums)-1, start, -1):
            if nums[r-1] > nums[r]:
                moved_r = True
                end = r
                break
        

        min_window, max_window = float("inf"), float("-inf")
        for i in range(start, end+1):
            min_window = min(min_window, nums[i])
            max_window = max(max_window, nums[i])
        
        i = start - 1
        while i >= 0 and nums[i] > min_window:
            start -= 1
            i -= 1
        
        j = end+1
        while j < len(nums) and nums[j] < max_window:
            end += 1
            j += 1
        
        if not moved_l and not moved_r:
            return 0
        else:
            return end-start+1