"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]

Example 2:
    Input: root = [3,9,8,4,0,1,7]
    Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
    Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
    Output: [[4],[2,5],[1,10,9,6],[3],[11]]
"""

from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        stack = [(0, root)]
        min_col, max_col = 0, 0
        res = defaultdict(list)

        while stack:
            curr_col, curr_node = stack.pop(0)
            res[curr_col].append(curr_node.val)
            if curr_node.left:
                stack.append((curr_col-1, curr_node.left))
                min_col = min(min_col, curr_col-1)
            if curr_node.right:
                stack.append((curr_col+1, curr_node.right))
                max_col = max(max_col, curr_col+1)
        
        return [res[key] for key in range(min_col, max_col+1)]