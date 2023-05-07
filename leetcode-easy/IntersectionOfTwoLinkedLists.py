""" PROMPT: Given the heads of two singly linked-lists headA and headB, 
    return the node at which the two lists intersect. 
    If the two linked lists have no intersection at all, return null.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # First approach with hash set
        # first_set = set()
        # curr = headA
    
        # while curr:
        #     first_set.add(curr)
        #     curr = curr.next
        
        # curr = headB
        # while curr:
        #     if curr in first_set:
        #         return curr
        #     curr = curr.next
        # return None


        # Second approach with two two pointers
        one = headA
        two = headB

        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one





