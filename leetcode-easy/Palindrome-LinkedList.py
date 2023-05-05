from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # USING Linear time and space - O(n) space and time

        # convert linked list to array 
        # lst = []
        # while head:
        #     lst.append(head.val)
        #     head = head.next
        # # check if palindrome
        # l, r = 0, len(lst)-1
        # while l <= r:
        #     if lst[l] != lst[r]:
        #         return False
        #     return True

        # USING O(n) time and O(1) space
        """
            Steps:
            - Use two pointer approach to find middle of list
            - Reverse second half of list
            - Using two pointers from front and end of reversed half, check if palindrome
        """
        slow, fast = head, head
        
        # Step 1. Find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Step 2. (slow is at or close to middle of list)
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        
        # Step 3. Check palindrome
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True







