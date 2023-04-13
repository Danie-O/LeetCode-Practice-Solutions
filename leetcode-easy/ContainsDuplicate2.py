from typing import List

""" PROMPT:

    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Naive Approach with hash set
        # hash_set = {}
        
        # for idx in range(len(nums)):
        #     # If condition is met, return true
        #     if nums[idx] in hash_set and abs(idx - hash_set[nums[idx]]) <= k:
        #         return True
        #     hash_set[nums[idx]] = idx
        # return False


        # Using sliding window
        window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k: # the condition is for abs(i-j) <= k
                # if size of the window becomes greater than k, remove the last visited element
                window.remove(nums[left])
                left += 1
            if nums[right] in window: # duplicate found
                return True
            window.add(nums[right])
        return False


# Examples
example = Solution()

# Example 1:
nums = [1,2,3,1]
k = 3
print(example.containsNearbyDuplicate(nums, k))
# Output: true


# Example 2:
nums2 = [1,0,1,1]
k2 = 1
print(example.containsNearbyDuplicate(nums2, k2))
# Output: true

# Example 2:
nums3 = [1,2,3,1,2,3]
k3 = 2
print(example.containsNearbyDuplicate(nums3, k3))
# Output: false
