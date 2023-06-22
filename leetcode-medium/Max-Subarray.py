class Solution:
    # TIME: O(N) => We iterate through array from second element so its approximately N times, 
    #               where N=length of input array
    # SPACE: O(1) => No extra memory is used as current max sum at each index is plugged back into the input 

    def maxSubArray(self, nums: List[int]) -> int:
        overall_max_sum = nums[0]

        for i in range(1, len(nums)):
            # for each element, update its value such that: 
            # the max sum is either its value or its value + the max sum of previous elements
            nums[i] = max(nums[i], nums[i] +  nums[i-1])

            # update the overall max_sum if current max_sum > than the overall_max_sum
            overall_max_sum = max(overall_max_sum, nums[i])
        return overall_max_sum

        