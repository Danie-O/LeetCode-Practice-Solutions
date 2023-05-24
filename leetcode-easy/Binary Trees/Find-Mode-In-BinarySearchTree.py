""" Prompt: 
    Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., 
    the most frequently occurred element) in it.

    If the tree has more than one mode, return them in any order. Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode_dict = {}
        max_mode = 0
        result = []

        def dfs(root: TreeNode):
            if not root: return

            mode_dict[root.val] = mode_dict.get(root.val, 0) + 1
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        max_mode = max(list(mode_dict.values()))

        for key, value in mode_dict.items():
            if value == max_mode:
                result.append(key)
        return result
