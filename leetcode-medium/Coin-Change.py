class Solution:
    # Optimised solution with DP(Bottom-Up)
    def coinChange(self, coins: List[int], amount: int) -> int:
        # define array to store min no of coins required to get amount, from 0 to amount
        dp = [amount + 1] * (amount + 1)
        # base case: when amount = 0, no of coins needed would be 0
        dp[0] = 0

        for amt in range(1, amount+1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        
        return dp[amount] if (dp[amount] != amount + 1) else -1


    # Using Greedy -> some test cases failed due to greedy not considering smaller elements
    # def coinChange(self, coins: List[int], amount: int) -> int:
    
    #     remainder, count = 0, 0
    #     if amount == 0:   # there is no zero(0) coin denomination
    #         return 0
    #     elif len(coins) == 1 and coins[0] == amount:
    #         return 1

    #     coins.sort()
    #     for i in range(len(coins) - 1, -1, -1):
    #         if amount >= coins[i]:
    #             quotient = amount // coins[i]
    #             count += quotient
    #             amount = amount - (quotient * coins[i])
    #             if not amount: return count
    #     return count if not amount else -1

