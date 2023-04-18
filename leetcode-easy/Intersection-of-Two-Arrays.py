from typing import List

""" PROMPT: Given two integer arrays nums1 and nums2, return an array of their intersection. 

Each element in the result must be unique and you may return the result in any order.
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # CONCISE SOLUTION.
        return list(set(nums1) & set(nums2))  # use logical AND property


# Examples
example = Solution()

# Example 1:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(example.intersection(nums1, nums2))
# Output: [2]
