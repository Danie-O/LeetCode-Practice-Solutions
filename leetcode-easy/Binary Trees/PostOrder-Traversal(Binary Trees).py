from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ Postorder: root.left -> root.right -> root"""
        
        # RECURSIVE SOLUTION
        # if not root:
        #     return []
        # return (self.postorderTraversal(root.left) + 
        #         self.postorderTraversal(root.right) + 
        #         [root.val]
        #         )

        # USING HELPER FUNCTION + RECURSION
        def traverse(node: TreeNode):
            if not node: return []
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            result.append(node.val)
        result = []
        traverse(root)
        return result
