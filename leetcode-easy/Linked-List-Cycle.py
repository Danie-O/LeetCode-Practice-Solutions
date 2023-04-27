""" PROMPT: Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using hashset. O(N) time, O(N) space
        # hashset = set()
        # while head:
        #     if head in hashset:
        #         return True
        #     hashset.add(head)
        #     head = head.next 
        # return False
    

        # Using two pointers. O(N) time, O(1) space
        # slow = head
        # fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        #     if slow == fast:
        #         return True 
        # return False


        # Using one pointer and assuming that value of unvisited nodes can't be none, and we don't need to reuse visited node values. 
        # O(N) time, O(1) space.
        slow = head

        while slow:
            if slow.val == None:
                return True
            slow.val = None # change value to show it has been visited
            slow = slow.next
        return False



# EXAMPLE 1:   
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# EXAMPLE 2:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.