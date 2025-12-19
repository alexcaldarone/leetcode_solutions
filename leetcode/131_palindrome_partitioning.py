"""
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

Example 2:
    Input: s = "a"
    Output: [["a"]]
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            if len(s) == 1:
                return True
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        
        n = len(s)
        res = []
        is_pal = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                if is_palindrome(s[i:j+1]):
                    is_pal[i][j] = 1
        
        def backtrack(s, i, curr):
            nonlocal res
            if i == n:
                res.append(curr.copy())
                return 
            for j in range(i, n):
                if is_pal[i][j]:
                    curr.append(s[i:j+1])
                    backtrack(s, j+1, curr)
                    curr.pop()
        
        backtrack(s, 0, [])
        return res