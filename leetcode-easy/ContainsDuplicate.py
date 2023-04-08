from collections import Counter

class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     hash_of_nums = {}
    #     for i in nums:
    #         if i in hash_of_nums:
    #             return True
    #         hash_of_nums[i] = True
    #     return False

    
    def containsDuplicate(self, nums) -> bool:
        hashmap = Counter(nums)
        for item in hashmap:
            if hashmap[item] >= 2:
                return True

        return False
