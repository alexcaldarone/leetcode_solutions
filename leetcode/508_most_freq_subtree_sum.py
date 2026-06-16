"""
Given the root of a binary tree, return the most frequent subtree sum. 
If there is a tie, return all the values with the highest frequency in any order.
The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

Example 1:
    Input: root = [5,2,-3]
    Output: [2,-3,4]

Example 2:
    Input: root = [5,2,-5]
    Output: [2]
"""

from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sums = defaultdict(int)

        def dfs(root):
            nonlocal sums
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            sums[left + root.val + right] += 1
            return left + right + root.val
        
        dfs(root)
        tmp = list(sums.values())
        maxfreq = max(tmp)
        if tmp.count(maxfreq) > 1:
            return [k for k, v in sums.items() if v == maxfreq]
        else:
            return [max(sums, key=sums.get)]
        
