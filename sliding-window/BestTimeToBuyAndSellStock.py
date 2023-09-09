from typing import List 

class Solution:
    # O(n) time, O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                curr_profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, curr_profit)
            else:
                left = right
            right += 1
        
        return maxProfit
        
sample = Solution()
print(sample.maxProfit([7,1,5,3,6,4])) # expected result = 5
print(sample.maxProfit([7,6,4,3,1])) # expected result = 0