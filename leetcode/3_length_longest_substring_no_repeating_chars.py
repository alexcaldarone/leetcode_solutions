"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()
        l = r = 0
        res = 0

        while r < len(s):
            chars[s[r]] += 1

            while chars[s[r]] > 1:
                chars[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
            r += 1

        return res