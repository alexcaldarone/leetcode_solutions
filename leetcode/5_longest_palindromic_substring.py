"""
Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        n = len(s)

        def dp(i, j):
            if i >= j:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == s[j]:
                memo[(i, j)] = dp(i + 1, j - 1)
            else:
                memo[(i, j)] = False

            return memo[(i, j)]

        max_len = 0
        start = 0

        for i in range(0, n):
            for j in range(i, n):
                if dp(i, j) and max_len < j - i + 1:
                    start = i
                    max_len = j - i + 1

        return s[start:start + max_len]