from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Trying hash map: O(n) time, O(n) space
        nums_map = {}
        
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1
        
        result = []
        for num in nums_map:
            if (len(nums) // 3) < nums_map[num]:
                result.append(num)
        return result

        # TODO: Come up with a solution that uses O(1) space

# Examples
s = Solution()

# Example 1:
nums1 = [3,2,3]
print(s.majorityElement(nums1))
# Output: [3]

# Example 2:
nums2 = [1]
print(s.majorityElement(nums2))
# Output: [1]

# Example 3:
nums3 = [1,2]
print(s.majorityElement(nums3))
# Output: [1,2]