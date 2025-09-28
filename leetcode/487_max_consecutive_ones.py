"""
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Example 1:
    Input: nums = [1,0,1,1,0]
    Output: 4
    Explanation: 
    - If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
    - If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
    The max number of consecutive ones is 4.

Example 2:
    Input: nums = [1,0,1,1,0,1]
    Output: 4
    Explanation: 
    - If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
    - If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
    The max number of consecutive ones is 4.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        j = 0
        count = 0
        best = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            if count > 1 and j < i:
                if nums[j] == 0:
                    count -= 1
                j += 1
            best = max(best, i-j+1)

        return best   