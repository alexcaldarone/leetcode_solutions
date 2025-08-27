"""
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:
    Input: root = [1,2,3,4,5,6,7]
    Output: [[1],[2,3],[4,5,6,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

Example 3:
    Input: root = []
    Output: []
"""

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)
        queue.append(None)

        curr_level = deque()
        reversed_layer = False
        # i do a normal bfs and just change how i add them to the list
        while queue:
            curr = queue.popleft()

            if curr:
                if not reversed_layer:
                    curr_level.append(curr.val)
                else:
                    curr_level.appendleft(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            else:
                # i have finished a layer
                res.append(list(curr_level))
                if len(queue) > 0:
                    queue.append(None)
                curr_level = deque()
                reversed_layer = not reversed_layer
        
        return res