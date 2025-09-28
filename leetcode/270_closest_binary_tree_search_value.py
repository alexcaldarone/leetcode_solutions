"""
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. 
If there are multiple answers, print the smallest.

Example 1:
    Input: root = [4,2,5,1,3], target = 3.714286
    Output: 4

Example 2:
    Input: root = [1], target = 4.428571
    Output: 1
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return
        
        # i want to do dfs: keep track of node and distance.
        # then, compute the distance to the current node.
        self.res = (root, abs(root.val - target))

        def dfs(root):
            if not root:
                return
            
            # if same, get smallest
            if abs(root.val - target) == self.res[1] and root.val < self.res[0].val:
                self.res = (root, abs(root.val - target))
            elif abs(root.val - target) < self.res[1]:
                self.res = (root, abs(root.val - target))
            
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        
        dfs(root)
        return self.res[0].val