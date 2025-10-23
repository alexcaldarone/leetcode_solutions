"""
Given a string s, you need to partition it into one or more balanced substrings. 
For example, if s == "ababcc" then ("abab", "c", "c"), ("ab", "abc", "c"), and ("ababcc") are all valid partitions, 
but ("a", "bab", "cc"), ("aba", "bc", "c"), and ("ab", "abcc") are not. The unbalanced substrings are bolded.

Return the minimum number of substrings that you can partition s into.

Note: A balanced string is a string where each character in the string occurs the same number of times.

Example 1:
    Input: s = "fabccddg"
    Output: 3
    Explanation:
    We can partition the string s into 3 substrings in one of the following ways: ("fab", "ccdd", "g"), or ("fabc", "cd", "dg").

Example 2:
    Input: s = "abababaccddb"
    Output: 2
    Explanation:
    We can partition the string s into 2 substrings like so: ("abab", "abaccddb").
"""

from collections import Counter

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n+1)]

        for i in range(1, n):
            count = Counter()
            for j in range(i, -1, -1):
                count[s[j]] += 1
                if self.is_valid(count):
                    dp[i+1] = min(dp[i+1], dp[j] + 1)

        return dp[-1]            

    def is_valid(self, c: dict) -> bool:
        # determines if a string is valid
        return len(set(c.values())) == 1
    
"""
Expalanation:
At first we initiate an array where each word is its own partition.
Then we iterate through the string, and for each character we count the frequency of each character in the substring from the current character to the beginning of the string.
If the substring is valid (all characters have the same frequency), we update the dp array to reflect the minimum number of partitions needed up to that point.
"""