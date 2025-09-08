"""
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].

Example 1:
    Input: n = 1
    Output: []

Example 2:
    Input: n = 12
    Output: [[2,6],[3,4],[2,2,3]]

Example 3:
    Input: n = 37
    Output: []
"""

class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return []
        
        res = []

        def backtrack(factors, rest, target):
            if factors:
                res.append(factors + [target])
            
            i = rest
            while i*i <= target:
                if target % i == 0:
                    backtrack(factors + [i], i, target//i)
                i += 1
        
        backtrack([], 2, n)
        return res