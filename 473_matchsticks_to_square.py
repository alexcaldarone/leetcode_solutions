"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. 
You want to use all the matchsticks to make one square. 
You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:
    Input: matchsticks = [1,1,2,2,2]
    Output: true
    Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:
    Input: matchsticks = [3,3,3,3,4]
    Output: false
    Explanation: You cannot find a way to form a square with all the matchsticks.
"""

from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        
        possible_side = sum(matchsticks)//4

        if sum(matchsticks) != 4*possible_side:
            return False
        
        matchsticks.sort(reverse=True)
        sums = [0 for _ in range(4)]

        def dfs(i):
            if i == len(matchsticks):
                return sums[0] == sums[1] == sums[2] == sums[3] == possible_side
            
            for j in range(4):
                if sums[j] + matchsticks[i] <= possible_side:
                    sums[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    
                    sums[j] -= matchsticks[i] # backtrack
            return False
        
        return dfs(0)
            
