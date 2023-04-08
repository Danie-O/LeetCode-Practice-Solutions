from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """ APPROACH 1 """
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        
        count = nums.count(val)
        while count:
            nums.remove(val)
            count -= 1

        """ SECOND APPROACH """
        # l, r = 0, len(nums) - 1

        # if len(nums) == 1 and nums[0] == val:
        #     nums.pop()
        #     return 0

        # while l < r:
        #     if nums[r] != val:
        #         if nums[l] == val:
        #             nums[l] = nums[r]
        #             r -= 1
        #         l += 1
        #     else:
        #         r -= 1
        # return l+1


nums = [3,2,2,3]
val = 3