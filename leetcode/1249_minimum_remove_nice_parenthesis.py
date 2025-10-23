"""
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:
    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
    Input: s = "a)b(c)d"
    Output: "ab(c)d"

Example 3:
    Input: s = "))(("
    Output: ""
    Explanation: An empty string is also valid.
"""

# this solution is slow (O(n) time, O(n) space), but i have to iterate through the string twice
# once to find the bad parentheses, and once to build the result string
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i, lett in enumerate(s):
            if lett in ('(', ')'):
                if lett == '(':
                    stack.append((i, lett))
                else:
                    if len(stack) > 0 and stack[-1][1] == '(':
                        stack.pop(-1)
                    else:
                        stack.append((i, lett))
        
        bad_idx = set([i for i, _ in stack])

        res = ''
        for i in range(0, len(s)):
            if i not in bad_idx:
                res += s[i]
        
        return res

