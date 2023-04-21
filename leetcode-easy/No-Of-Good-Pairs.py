from typing import List

""" PROMPT: Given an array of integers nums, return the number of good pairs.

    A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Solution 1: nested loop
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
        # Solution 2: sorting + two pointers
        # Solution 3: using collections.Counter
        pass
