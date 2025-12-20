"""
Given an integer n, return the number of structurally unique BST's (binary search trees) 
which has exactly n nodes of unique values from 1 to n.

Example 1:
    Input: n = 3
    Output: 5

Example 2:
    Input: n = 1
    Output: 1
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            res = 0
            for k in range(1, i+1):
                res += dp[i-k]*dp[k-1]
            
            dp[i] = res
        
        return dp[n]