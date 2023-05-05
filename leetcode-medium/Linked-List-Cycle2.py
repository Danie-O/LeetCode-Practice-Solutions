""" PROMPT: Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
    It is -1 if there is no cycle. 
    ** Note that pos is not passed as a parameter. Do not modify the linked list.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Steps:
            - Use Floyd's cycle algo with 2 pointers to find where cycle exists
            - Start another cycle with head and slow, and return head when head reaches slow
        """    
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # if we encounter a cycle, reset slow to head of linked list
            # continue until slow reaches the beginning of the cycle and return slow
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None




