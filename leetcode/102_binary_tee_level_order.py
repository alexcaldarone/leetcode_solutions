"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []    
    Output: []
"""

from collections import defaultdict
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [(root, 0)]
        nodes = defaultdict(list)
        
        while q:
            node, level = q.pop(0)
            nodes[level].append(node.val)

            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        
        return [lis for _, lis in nodes.items()]