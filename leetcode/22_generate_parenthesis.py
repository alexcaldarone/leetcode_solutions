"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        def backtrack(open_used, close_used, s):
            if open_used == n and close_used == n:
                res.add(s)
                return
            if open_used < n:
                backtrack(open_used + 1, close_used, s + "(")
            if close_used < open_used:
                backtrack(open_used, close_used + 1, s + ")")

        backtrack(0, 0, "")
        return list(res)