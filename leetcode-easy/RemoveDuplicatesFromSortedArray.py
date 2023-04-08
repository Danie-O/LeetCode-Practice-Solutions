from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = 1
        
        # return 0 if array is empty
        if len(nums) == 0:
            return len(nums)

        while r < len(nums):
            # if number at right is not unique
            # (since nums is sorted, it would have the same no. before it if duplicate)
            if nums[r] == nums[r-1]:
                r += 1
            else:
                nums[l] = nums[r] # replace left value with the next unique item
                l += 1
                r += 1
        return l
            


nums = [1,1,2]