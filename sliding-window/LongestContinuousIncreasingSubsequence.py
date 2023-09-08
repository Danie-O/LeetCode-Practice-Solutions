"""Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). 
    The subsequence must be strictly increasing.
    A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is;
        [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 
Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.

    Returns:
        _type_: _description_
"""


class Solution:
    # O(n) time: we slide through entire array exactly once
    # O(1) space: no auxilliary data structure utilised
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        
        max_length = 0
        i, j = 0, 0

        while j < len(nums):
            j += 1
            max_length = max(max_length, j - i)
            if j < len(nums) and nums[j - 1] >= nums[j]:
                # reset window since condition not satisfied
                i = j
        return max_length