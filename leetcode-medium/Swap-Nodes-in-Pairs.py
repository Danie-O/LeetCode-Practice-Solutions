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
        pass