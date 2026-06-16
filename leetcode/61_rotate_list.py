"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]

Example 2:
    Input: head = [0,1,2], k = 4
    Output: [2,0,1]
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        
        head2 = head
        n = 0
        while head2:
            n += 1
            head2 = head2.next
        
        rotations = k % n
        if rotations == 0:
            return head
        new_head = None
        dummy = head
        # iterate to find new head position, and place it
        for _ in range(n-rotations):
            dummy = dummy.next
        new_head = dummy
        new_tail = head
        # iterate until end
        for _ in range(n-rotations-1):
            new_tail = new_tail.next
        new_tail.next = None
        dummy2 = new_head
        for _ in range(n-rotations, n-1):
            dummy2 = dummy2.next
        dummy2.next = head
        return new_head
        