"""
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. 
Each minute, you may take either the leftmost character of s, or the rightmost character of s.
Return the minimum number of minutes needed for you to take at least k of each character,
or return -1 if it is not possible to take k of each character.

Example 1:
    Input: s = "aabaaaacaabc", k = 2
    Output: 8
    Explanation: 
        Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
        Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
        A total of 3 + 5 = 8 minutes is needed.
        It can be proven that 8 is the minimum number of minutes needed.

Example 2:
    Input: s = "a", k = 1
    Output: -1
    Explanation: It is not possible to take one 'b' or 'c' so return -1.
"""

from collections import defaultdict

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        for lett in s:
            counts[lett] += 1
        
        for lett in ("a", "b", "c"):
            if counts[lett] < k:
                return -1
        
        max_len = 0
        taken = {"a": 0, "b": 0, "c": 0}
        l = 0

        for r in range(len(s)):
            taken[s[r]] += 1

            while any(val > counts[key] - k for key, val in taken.items()):
                taken[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r-l+1)
            
        
        return len(s) - max_len