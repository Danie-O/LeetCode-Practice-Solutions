from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # TIME COMPLEXITY: O(N); SPACE COMPLEXITY: O(1) --->ignoring the recursive stack
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node:TreeNode, left, right):
            if not node: return True

            if not (node.val < right and node.val > left):
                return False
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        
        return valid(root, float('-inf'), float("inf"))