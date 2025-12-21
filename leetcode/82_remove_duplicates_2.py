"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
    Input: head = [1,2,3,3,4,4,5]
    Output: [1,2,5]

Example 2:
    Input: head = [1,1,1,2,3]
    Output: [2,3]
"""

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        left = head
        right = head.next
        while right:
            if left.val == right.val:
                while right and left.val == right.val:
                    right = right.next
                
                prev.next = right
                
                if right:
                    left = right
                    right = right.next
                else:
                    left = None
            else:
                prev = left
                left = right
                right = right.next    
        
        return dummy.next