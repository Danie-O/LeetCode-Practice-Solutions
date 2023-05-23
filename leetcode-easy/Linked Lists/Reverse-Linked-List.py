""" PROMPT: Given the head of a singly linked list, reverse the list, and return the reversed list."""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # Initialise previous pointer as NULL(end of linked list)
        curr = head # Let current pointer be head of linked list

        # Run loop until we get to end of oringinal linked list
        while curr:
            # Let next node to visit be the next node of current node
            next_node = curr.next

            # Change direction of current node by making its next pointer point to the preceeding node in original linked list
            curr.next = prev

            # Update previous and current pointers
            prev, curr = curr, next_node
        return prev


# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = []
# Output: []