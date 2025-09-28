"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

Example 1:
    Input: nums = [1,1,2,1,1], k = 3
    Output: 2
    Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
    Input: nums = [2,4,6], k = 1
    Output: 0
    Explanation: There are no odd numbers in the array.

Example 3:
    Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    Output: 16
"""

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        l = res = n_odd = subs = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 1: # odd
                n_odd += 1
            
            if n_odd == k:
                subs = 0            
                while n_odd == k:
                    if nums[l] % 2 == 1:
                        n_odd -= 1
                    subs += 1
                    l += 1
            res += subs
        
        return res