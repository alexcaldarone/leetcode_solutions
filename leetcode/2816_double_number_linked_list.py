"""
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
Return the head of the linked list after doubling it.

Example 1:
    Input: head = [1,8,9]
    Output: [3,7,8]
    Explanation: The linked list represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

Example 2:
    Input: head = [9,9,9]
    Output: [1,9,9,8]
    Explanation: The linked list represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
"""

from typing import Optional
from math import log10, floor

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        curr = head
        n = 0
        # get length of linked list, will be used for powers of 10
        while head:
            n += 1
            head = head.next

        for i in range(n): # iterate over all linked list
            s += curr.val * 10**(n-i)
            curr = curr.next

        s_mult = 2*s
        # only edge case if number was just 0, we can return it
        if s_mult == 0:
            return ListNode(0)
        n2 = floor(log10(s_mult))
        res_head = curr2 = ListNode(None)

        for i in range(n2, 0, -1): # iterate over number of digits
            # write number
            tmp = s_mult // 10**i
            curr2.next = ListNode(tmp)
            curr2 = curr2.next
            s_mult -= tmp*10**i
        
        return res_head.next
    
# official solution (faster and cleaner)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val = 0
        values = []

        while head is not None:
            values.append(head.val)
            head = head.next
        
        new_tail = None

        while values or val != 0:
            new_tail = ListNode(0, new_tail)
            if values:
                val += values.pop() * 2
            new_tail.val = val % 10
            val //= 10
        
        return new_tail