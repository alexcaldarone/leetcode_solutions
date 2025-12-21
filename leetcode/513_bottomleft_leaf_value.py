"""
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
    Input: root = [2,1,3]
    Output: 1

Example 2:
    Input: root = [1,2,3,4,null,5,6,null,null,7]
    Output: 7
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = root.val

        while q:
            # take all nodes out, and record minimum in a row
            nodes = len(q)
            for i in range(nodes):
                node = q.popleft()
                if i == 0:
                    ans = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ans