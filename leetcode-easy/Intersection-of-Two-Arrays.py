from typing import List

""" PROMPT: Given two integer arrays nums1 and nums2, return an array of their intersection. 

Each element in the result must be unique and you may return the result in any order.
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # CONCISE SOLUTION.
        return list(set(nums1) & set(nums2))  # use logical AND property

        # SECOND APPROACH
        # set1 = set(nums1)
        # set2 = set(nums2)
        # res = []

        # for num in set1:
        #     if num in set2:
        #         res.append(num)

        # return res


# Examples
example = Solution()

# Example 1:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(example.intersection(nums1, nums2))
# Output: [2]
