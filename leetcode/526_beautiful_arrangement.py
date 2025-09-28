"""
Suppose you have n integers labeled 1 through n. 
A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:
- perm[i] is divisible by i.
- i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

Example 1:
    Input: n = 2
    Output: 2
    Explanation: 
    The first beautiful arrangement is [1,2]:
        - perm[1] = 1 is divisible by i = 1
        - perm[2] = 2 is divisible by i = 2
    The second beautiful arrangement is [2,1]:
        - perm[1] = 2 is divisible by i = 1
        - i = 2 is divisible by perm[2] = 1

Example 2:
    Input: n = 1
    Output: 1
"""

# this solution is 5th percentile speed, so can be definetly made faster. how?
class Solution:
    def countArrangement(self, n: int) -> int:
        def is_beautiful(arr):
            for i, el in enumerate(arr):
                if arr[i] % (i+1) != 0 and (i+1)%arr[i] != 0:
                    #print(arr, arr[i], i+1)
                    return False
            return True
        
        res = 0
        # if i do it like this where is the dp?
        def backtrack(used, curr):
            nonlocal res
            if len(curr) == n:
                if is_beautiful(curr):
                    res += 1
                    return
            
            for i in range(1, n+1):
                if not used[i]:
                    used[i] = True
                    curr.append(i)
                    if is_beautiful(curr): # each subarray has to be beautiful
                        backtrack(used, curr)
                    used[i] = False
                    curr.pop()
        
        backtrack([False] * (n+1), [])
        return res