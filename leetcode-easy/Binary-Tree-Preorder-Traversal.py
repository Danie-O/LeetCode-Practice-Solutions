from typing import Optional, List

# Preorder traversal means:
# root -> root.left -> root.right 
# PS. root.left and root.right can be root nodes if they have children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            # def dfs(node):
            #     if not node: return

            #     ans.append(node.val)
            #     dfs(node.left)
            #     dfs(node.right)
            #     return   
        
            # ans = []
            
            # dfs(root)
            # return ans

        # SHORTER SOLUTION --> O(N) time and O(N) space
        if not root:
            return []
        else:
            return ([root.val] + 
                    self.preorderTraversal(root.left) + 
                    self.preorderTraversal(root.right)
                )

        #  ITERATIVE SOLUTION --> O(N) time and O(N) space**
        # head = root
        # stack = []
        # res = []

        # while head or stack:
        #     if head:
        #         res.append(head.val)
        #         if head.right:
        #             stack.append(head.right)
        #         head = head.left
        #     else:
        #         head = stack.pop()

        # return res   
