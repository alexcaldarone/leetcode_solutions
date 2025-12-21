"""
Given a sorted integer array nums and three integers a, b and c, 
apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, 
and return the array in a sorted order.

Example 1:
    Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
    Output: [3,9,15,33]

Example 2:
    Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
    Output: [-23,-5,1,7]
"""

from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def f(x, a, b, c):
            return a*x**2 + b*x + c

        n = len(nums)
        res = [0] * n
        l, r = 0, n-1

        k = n-1 if a >= 0 else 0
        if a >= 0:
            while l <= r:
                fl = f(nums[l], a, b, c)
                fr = f(nums[r], a, b, c)

                res[k] = fl if fl > fr else fr

                if fl > fr:
                    l += 1
                else:
                    r -= 1
                
                k -= 1
        else:
            while l <= r:
                fl = f(nums[l], a, b, c)
                fr = f(nums[r], a, b, c)

                res[k] = fl if fl < fr else fr

                if fl < fr:
                    l += 1
                else:
                    r -= 1
                
                k += 1

        return res