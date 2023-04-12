from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Trying hash map: O(n) time, O(n) space
        nums_map = {}
        
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1
            if (len(nums) // 2) < nums_map[num]:
                return num

        # for num in nums_map:
        #     if (len(nums)) // 2 < nums_map[num]:
        #         return num

# Examples
s = Solution()

# Example 1:
nums1 = [3,2,3]
print(s.majorityElement(nums1))
# Output: 3

# Example 2:
nums2 = [2,2,1,1,1,2,2]
print(s.majorityElement(nums2))
# Output: 2