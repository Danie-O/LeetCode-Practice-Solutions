class Solution:
    # Time: O(n), to traverse input array
    # Space: O(1), since input array does not count as extra memory
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
         
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer