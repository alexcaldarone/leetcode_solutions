"""
Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.
The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.
A subarray is a contiguous part of an array.

Example 1:
    Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
    Output: 20
    Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

Example 2:
    Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
    Output: 29
    Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

Example 3:
    Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
    Output: 31
    Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.
"""

class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        def maxPrefix(l):
            # get max prefix of length l
            window = sum(nums[:l])
            pref = [window]
            
            for start in range(1, n - l + 1):
                window += nums[start + l - 1] - nums[start - 1]
                pref.append(max(pref[-1], window))
            
            return pref
        
        def maxPostfix(l):
            # get max post fix of length l
            window = sum(nums[n - l:])
            suff = [0] * (n - l + 1)
            suff[n - l] = window
            
            for start in range(n - l - 1, -1, -1):
                window += nums[start] - nums[start + l]
                suff[start] = max(suff[start + 1], window)
            return suff
        
        prefFirst, postFirst = maxPrefix(firstLen), maxPostfix(firstLen)
        prefSecond, postSecond = maxPrefix(secondLen), maxPostfix(secondLen)

        res = 0

        for i in range(firstLen-1, n-secondLen):
            res = max(res, prefFirst[i-firstLen+1]+postSecond[i+1])
        for i in range(secondLen-1, n-firstLen):
            res = max(res, prefSecond[i-secondLen+1]+postFirst[i+1])
        
        return res