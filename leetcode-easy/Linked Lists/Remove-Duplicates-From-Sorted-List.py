from typing import Optional

"""PROMPT: 
    Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
    Return the linked list sorted as well.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        left = head

        # if not head:
        #     return None
        while left and left.next:
            if left.val == left.next.val:
                left.next = left.next.next
            else:
                left = left.next
        return dummy.next
