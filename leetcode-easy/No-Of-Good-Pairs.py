from typing import List

""" PROMPT: Given an array of integers nums, return the number of good pairs.

    A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Solution 1: nested loop
        # pairs = 0
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             pairs += 1
        # return pairs

        # Solution 2: sorting + two pointers
        l, r = 0, 1
        pairs = 0
        nums.sort()  # sort list in-place

        while r < len(nums):
            if nums[l] == nums[r]:
                pairs += r - l
            else:
                l = r
            r += 1
        return pairs

        # Solution 3: using collections.Counter
        pass
