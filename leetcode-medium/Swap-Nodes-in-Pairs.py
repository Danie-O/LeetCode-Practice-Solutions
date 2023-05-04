""" PROMPT: Given a linked list, swap every two adjacent nodes and return its head.

    You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev, curr = dummy, head
        while curr and curr.next:
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            prev, curr = curr, curr.next
        return dummy.next

        # using recursion
        # def swapPairs(self, head):
        #     if not head or not head.next: return head

        #     new_start = head.next.next
        #     head, head.next = head.next, head
        #     head.next.next = self.swapPairs(new_start)
        #     return head



            
