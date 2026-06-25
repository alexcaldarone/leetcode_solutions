"""
You are given an array of strings equations that represent relationships between variables where each string equations[i] 
is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".
Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.
Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

Example 1:
    Input: equations = ["a==b","b!=a"]
    Output: false
    Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
    There is no way to assign the variables to satisfy both equations.

Example 2:
    Input: equations = ["b==a","a==b"]
    Output: true
    Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
"""

from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        node_ids = set()
        for st in equations:
            node_ids.add(st[0])
            node_ids.add(st[3])
        
        node_ids = {node: i for i, node in enumerate(node_ids)}
        parents = [i for i in range(len(node_ids))]
        size = [1] * len(parents)

        def _find(x, parents):
            if parents[x] != x:
                parents[x] = _find(parents[x], parents)
            return parents[x]

        def _union(a, b):
            nonlocal node_ids
            nonlocal size
            nonlocal parents

            root_a = _find(node_ids[a], parents)
            root_b = _find(node_ids[b], parents)

            if root_a == root_b:
                return False
            
            if size[root_a] == size[root_b]:
                root_a, root_b = root_b, root_a

            parents[root_b] = root_a
            return True
        
        # process equalities
        for st in equations:
            if st[1:3] == "==":
                _union(st[0], st[3])
        
        # process inequalities
        for st in equations:
            if st[1:3] == "!=":
                if _find(node_ids[st[0]], parents) == _find(node_ids[st[3]], parents):
                    return False
        
        return True
