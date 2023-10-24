# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            size = len(queue)
            curr_max = float('-inf')

            for i in range(size):
                curr = queue.popleft()
                curr_max = max(curr_max, curr.val)

                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            res.append(curr_max)
        
        return res
