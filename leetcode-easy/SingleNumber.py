from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ OPTIMISED SOLUTION USING BIT MANIPULATION WITH XOR: O(n) time & O(1) space """
        # Recall that n XOR(^) 0 = n. 
        # Using this intuition, applying XOR with each num in nums,
        # results in the unique number being equal to n at the end
        
        result = 0
        for num in nums:
            result ^= num 
        return result


        """ NAIVE SOLUTION: O(nlog n) time on average, O(n) space in worst case due to sorting

            # if nums contains only one element, it's unique so return it
            if len(nums) == 1:
            return nums[0]

            # sort array so repeated numbers are beside each other
            nums.sort()
            # return first element if next element is not equal to it
            if nums[0] != nums[1]:
                return nums[0]
            
            for i in range(1, len(nums) - 1):
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    return nums[i]

            if nums[i + 1] != nums[i]:
                return nums[i + 1]
        """
s = Solution()
# Example 1:
nums1 = [2,2,1]
print(s.singleNumber(nums1))
# Output: 1

# Example 2:
nums2 = [4,1,2,1,2]
print(s.singleNumber(nums2))
# Output: 4