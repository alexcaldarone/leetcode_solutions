"""
Given the root of a binary tree, return the number of uni-value subtrees.
A uni-value subtree means all nodes of the subtree have the same value.

Example 1:
    Input: root = [5,1,5,5,5,null,5]
    Output: 4

Example 2:
    Input: root = []
    Output: 0

Example 3:
    Input: root = [5,5,5,5,5,null,5]
    Output: 6
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        def is_valid(root):
            nonlocal res
            if not root:
                return True
            
            left_valid = is_valid(root.left)
            right_valid = is_valid(root.right)

            if left_valid and right_valid:
                if root.right and root.left and root.right.val == root.left.val == root.val \
                    or (root.left and not root.right and root.left.val == root.val) \
                    or (root.right and not root.left and root.right.val == root.val) \
                    or (not root.right and not root.left):
                    res += 1
                    return True
            
            return False
            
        is_valid(root)
        return res