"""PROMPT: Given the head of a linked list and an integer val, 
    remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = dummy = ListNode()
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
        return dummy.next
