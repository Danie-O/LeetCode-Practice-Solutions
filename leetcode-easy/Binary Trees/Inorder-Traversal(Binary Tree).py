from typing import Optional, List

# Inorder traversal means:
# root.left -> root -> root.right


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root: return []

        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # USING ARRAY
        result = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            result.append(current_node.val)
            if current_node.right:
                traverse(current_node.right)
        if root:
            traverse(root)
        return result

