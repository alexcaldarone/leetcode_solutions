"""
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

Example 1:
    Input: n = 2
    Output: 91
    Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

Example 2:
    Input: n = 0
    Output: 1
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 10

        for i in range(2, n+1):
            res = 9 # i can consider 1,...,9 as first digit
            for j in range(2, i+1):
                res *= (9-j+2)
            dp[i] = dp[i-1] + res
        
        return dp[n]