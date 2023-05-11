from typing import Optional
""" PROMPT: Given the roots of two binary trees root and subRoot, 
    return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
    The tree tree could also be considered as a subtree of itself.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """ Time complexity: O(s + t) """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t: 
            # an empty subtree is a subtree of the other if tree is empty or not
            return True
        if not s:
            # t cannot be subtree of an empty tree(s) if t is non-empty 
            return False

        # recall that the tree(s) is considered a subtree of itself 
        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    # helper function to check if subtree is the same as main tree
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False
