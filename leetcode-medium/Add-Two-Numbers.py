from typing import Optional

""" PROMPT: You are given two non-empty linked lists representing two non-negative integers. 

    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #calculate sum
            sumval = v1 + v2 + carry
            carry = sumval // 10
            sumval = sumval % 10
            current.next = ListNode(sumval)

            #update pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
    

# Examples
example = Solution()

# Example 1:
# Input: 
l1 = [2,4,3]
l2 = [5,6,4]
print(example.addTwoNumbers(l1, l2))
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: 
l1 = [0]
l2 = [0]
print(example.addTwoNumbers(l1, l2))
# Output: [0]