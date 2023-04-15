from typing import List

""" PROMPT:

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # FIRST APPROACH: FOR I IN ARRAY, IF I == 0: POP NUMS[I] AND APPEND IT
        # l, i = len(nums), 0
        # for i in range(l):
        #     if nums[i] == 0:
        #         temp = nums[i]
        #         nums.pop(i)
        #         nums.append(temp)
        # TODO: Fix error for case in which two zeroes are next to each other


        # SECOND APPROACH: TWO POINTERS
        left = 0 #slow pointer
        for right in range(len(nums)): # fast pointer
            if nums[right] != 0 and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]

            # wait while we find a non-zero element to swap with you
            if nums[left] != 0:
                left += 1


# Examples
example = Solution()

# Example 1:
nums = [0,1,0,3,12]
print(nums)
example.moveZeroes(nums)
print(nums)
# Output: [1,3,12,0,0]

# Example 2:
nums = [0]
print(nums)
example.moveZeroes(nums)
print(nums)
# Output: [0]