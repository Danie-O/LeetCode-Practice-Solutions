class Solution:
    # USING FLOYD'S CYCLE ALGORITHM (O(1) space, O(logN) time)
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)

        while fast != 1 and slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
        return fast == 1

    # USING HASHSET (O(N) space & time)
    # def isHappy(self, n: int) -> bool:
    #     visited = set()

    #     if n == 1:
    #         return True

    #     while n not in visited:
    #         visited.add(n)
    #         n = self.sumOfSquares(n)
    #         if n == 1:
    #             return True # (avoid going 1 iteration of infinite loop once n==1)
    #     return False

    # Helper function to calculate sum of square of digits in n

    def sumOfSquares(self, n: int) -> int:
        total = 0
        while n:
            temp = n % 10
            total += (temp ** 2)
            n = n // 10
        return total


# Examples
example = Solution()

# Example 1:
n = 19
print(example.isHappy(n))
# Output: True
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


# Example 2:
n = 2
print(example.isHappy(n))
# Output: False
# Explanation: eventually, the sum of squares would result in a cycle at a number not equal to 1
