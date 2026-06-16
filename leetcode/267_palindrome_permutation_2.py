"""
Given a string s, return all the palindromic permutations (without duplicates) of it.
You may return the answer in any order. If s has no palindromic permutation, return an empty list.

Example 1:
    Input: s = "aabb"
    Output: ["abba","baab"]

Example 2:
    Input: s = "abc"
    Output: []
"""

from typing import List

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def _is_palindrome(s_in, odd):
            if odd:
                s = s_in + odd[0] + s_in[::-1]
            else:
                s = s_in + s_in[::-1]
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        counts = Counter(s)
        if len(counts.keys()) == 1:
            return [s]
        if len([v for k,v in counts.items() if v % 2 == 1]) > 1:
            return []
        odd = [k for k,v in counts.items() if v % 2 == 1]
        candidates = {k: v//2 for k,v in counts.items()}
        res = set()
        used = defaultdict(int)

        def backtrack(curr, used):
            nonlocal s
            nonlocal res
            nonlocal odd
            nonlocal candidates
            if len(curr) == len(s)//2 and _is_palindrome(curr, odd):
                if odd:
                    s = curr + odd[0] + curr[::-1]
                else:
                    s = curr + curr[::-1]
                res.add(s)
                return
            
            for lett, freq in candidates.items():
                if used[lett] < freq:
                    used[lett] += 1
                    backtrack(curr + lett, used)
                    used[lett] -= 1
        
        backtrack("", used)
        return list(res)
