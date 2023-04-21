from typing import List
from collections import Counter

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
        # l, r = 0, 1
        # pairs = 0
        # nums.sort()  # sort list in-place

        # while r < len(nums):
        #     if nums[l] == nums[r]:
        #         pairs += r - l
        #     else:
        #         l = r
        #     r += 1
        # return pairs

        # Solution 3: using collections.Counter
        # with this approach, we need to consider the fact that the number of possible
        # pairs = combinations of numbers
        counts = Counter(nums)
        pairs = 0

        for count in counts.values():
            pairs += (count * (count-1)) // 2

        return pairs


# Examples
example = Solution()

# Example 1:
nums = [1, 2, 3, 1, 1, 3]
print(example.numIdenticalPairs(nums))
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
nums = [1, 1, 1, 1]
print(example.numIdenticalPairs(nums))
# Output: 6
# Explanation: Each pair in the array are good.

# Example 3:
nums = [1, 2, 3]
print(example.numIdenticalPairs(nums))
# Output: 0
# Explanation: There are no identical pairs in input list.
