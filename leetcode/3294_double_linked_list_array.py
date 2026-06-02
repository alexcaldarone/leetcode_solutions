"""
You are given an arbitrary node from a doubly linked list, which contains nodes that have a next pointer and a previous pointer.
Return an integer array which contains the elements of the linked list in order.

Example 1:
    Input: head = [1,2,3,4,5], node = 5
    Output: [1,2,3,4,5]

Example 2:
    Input: head = [4,5,6,7,8], node = 8
    Output: [4,5,6,7,8]
"""

from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def toArray(self, node: Optional[Node]) -> List[int]:
        while node.prev:
            node = node.prev
        
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        
        return arr