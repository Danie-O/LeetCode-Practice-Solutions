from typing import Optional

""" PROMPT: Given a binary tree, determine if it is height-balanced.

    Note.
        A tree is height-balanced if the height of the left and right sub-trees of every node differ in height by at most 1.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        # return self.isBalanced(root.left) == self.isBalanced(root.right)

        def dfs(root) -> list(bool, int):
            if not root:
                return [True, 0]

            # recursively return whether left and right subtrees are balanced, and their heights
            left, right = dfs(root.left), dfs(root.right)

            # if either left or right subtree of a root is imbalanced, that root would be imbalanced eventually
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

        