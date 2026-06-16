"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
    - Collect all the leaf nodes.
    - Remove all the leaf nodes.
    - Repeat until the tree is empty.

Example 1:
    Input: root = [1,2,3,4,5]
    Output: [[4,5,3],[2],[1]]
    Explanation:
        [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does 
        not matter the order on which elements are returned.

Example 2:
    Input: root = [1]
    Output: [[1]]
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        parent = {}
        children = {}
        parent[root] = None
        def dfs(root):
            nonlocal children
            nonlocal parent

            children[root] = 0
            if root.left:
                parent[root.left] = root
                children[root] += 1
                dfs(root.left)
            if root.right:
                parent[root.right] = root
                children[root] += 1
                dfs(root.right)
        
        dfs(root)
        q = []
        for node, n_children in children.items():
            if n_children == 0:
                q.append((node, n_children))
        res = []
        while q:
            tmp = []
            curr = []
            for i in range(len(q)):
                curr.append(q[i][0])
                tmp.append(q[i][0].val)
            
            while q:
                q.pop()
            
            for node in curr:
                par = parent[node]
                if par:
                    children[par] -= 1
                    if children[par] == 0:
                        q.append((par, 0))
                
            res.append(tmp)
        
        return res