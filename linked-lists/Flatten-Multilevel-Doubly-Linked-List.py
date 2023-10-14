"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr is not None:
            # if curr has child, merge child level to parent level
            if curr.child:
                self.merge(curr)
            curr = curr.next

        return head
    
    def merge(self, current):
        child = current.child

        # traverse until child.next is none(end of child list)
        # then let current point to its child, and end of child list point to next node in previous level
        while child.next:
            child = child.next
        
        if current.next: # if current is not the end of list
            # now, update child and current.next
            child.next = current.next
            current.next.prev = child
            
        # update current and current.child to point to each other
        current.next = current.child
        current.child.prev = current
        
        # remove the child pointer
        current.child = None

        