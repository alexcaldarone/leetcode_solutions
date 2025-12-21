"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:
    Input: coins = [2], amount = 3
    Output: -1

Example 3:
    Input: coins = [1], amount = 0
    Output: 0
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        res = float("inf")
        min_coin = min(coins)
        
        def dfs(i, n, curr):
            nonlocal res
            # base case
            if n == 0:
                res = min(res, curr)
                return
            
            if n < min_coin:
                return

            if i >= len(coins):
                return

            all_used = n // coins[i]
            for j in range(all_used, -1, -1):
                if j + curr >= res:
                    return
                dfs(i+1, n-j*coins[i], curr+j)
        
        dfs(0, amount, 0)
        return res if res != float("inf") else -1