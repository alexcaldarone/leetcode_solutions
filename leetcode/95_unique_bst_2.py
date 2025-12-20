"""
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
    Input: n = 3
    Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
    Input: n = 1
    Output: [[1]]
"""

from typing import List, Optional
from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        @cache
        def f(l, r):
            if l >= r:
                return [None]
            
            res = []
            for i in range(l, r):
                lows = f(l, i)
                highs = f(i+1, r)

                for t1 in lows:
                    for t2 in highs:
                        temp = TreeNode(i)
                        temp.left = t1
                        temp.right = t2
                        res.append(temp)
            
            return res
        
        return f(1, n+1)