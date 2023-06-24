class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        
        # A.
        # for i in range(len(ans)):
        #     ans[i] = nums[i] if i < n else nums[i - n]

        # B.
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans