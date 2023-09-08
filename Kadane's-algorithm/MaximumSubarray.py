"""Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

    Returns:
        _type_: _description_
"""


class Solution:
    # TIME: O(N) => We iterate through array from second element so its approximately N times, 
    #               where N=length of input array
    # SPACE: O(1) => No extra memory is used as current max sum at each index is plugged back into the input 

    # USING KADANE'S ALGO. AND MUTATING THE INPUT ARRAY
    def maxSubArray(self, nums: List[int]) -> int:
        overall_max_sum = nums[0]

        for i in range(1, len(nums)):
            # for each element, update its value such that: 
            # the max sum is either its value or its value + the max sum of previous elements
            nums[i] = max(nums[i], nums[i] +  nums[i-1])

            # update the overall max_sum if current max_sum > than the overall_max_sum
            overall_max_sum = max(overall_max_sum, nums[i])
        return overall_max_sum

    # USING KADANE'S ALGO. WITHOUT MUTATING THE INPUT ARRAY
    def maxSubArray(self, nums: List[int]) -> int:
        overall_max_sum = nums[0]
        current_sum = 0
        for num in nums:
            # do not consider negative predecessor for positive number
            if current_sum < 0:
                current_sum = 0
            current_sum = max(num, num +  current_sum)

            # update the overall max_sum if current max_sum > than the overall_max_sum
            overall_max_sum = max(overall_max_sum, current_sum)
        return overall_max_sum

        