""" PROMPT:

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # FIRST APPROACH: FOR I IN ARRAY, IF I == 0: POP NUMS[I] AND APPEND IT
        l = len(nums)
        i = 0
        # for i in range(l):
        while i < l:
            if nums[i] == 0:
            # if nums[i] == 0:
                temp = nums[i]
                nums.pop(i)
                nums.append(temp)
                i -= 1
            else:
                i += 1
        

        # SECOND APPROACH: TWO POINTERS
        # l, r = 0, 0
