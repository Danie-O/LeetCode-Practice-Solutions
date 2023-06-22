class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # SOLUTION 1: O(n) time, O(n) space
        # value_to_index_map = {}  # val -> index

        # for i, n in enumerate(nums):
        #     difference = target - n
        #     if difference in value_to_index_map:
        #         return [value_to_index_map[difference], i]
                
        #     value_to_index_map[n] = i

        # SOLUTION 2: 
        # O(nlog(n)) time => due to sorting, other operations are O(n), so overall it's O(nlog(n))
        # O(n) space => because we make a copy of the original array
        import copy
        nums2 = copy.copy(nums)
        nums.sort()
        l, r = 0, len(nums)-1

        while l < r:
            if nums[l] + nums[r] == target:
                index1 = nums2.index(nums[l])
                nums2[index1] = None # change value incase the numbers are the same
                index2 = nums2.index(nums[r])
                return [index1, index2]
            elif nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1 



