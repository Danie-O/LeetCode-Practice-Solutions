"""PROMPT:
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

import math


class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        isNeg = 0 # assume number is positive (not negative)
        # x_dup = x

        if x == 0:
            return x
        elif x < 0:
            x = abs(x)
            isNeg = 1
        
        while x:
            temp = x % 10
            res = res * 10 + temp
            x = x // 10

        if -2**31 <= res <= 2**31:
            if isNeg:
                return -res
            else:
                return res
                # return (x_dup // abs(x_dup)) * res
        else:
            return 0

        # Solution using Bit Manipulation
        # def reverse(self, x: int) -> int:
        # # Integer.MAX_VALUE = 2147483647 (end with 7)
        # # Integer.MIN_VALUE = -2147483648 (end with -8 )

        # MIN = -2147483648  # -2^31,
        # MAX = 2147483647  #  2^31 - 1

        # res = 0
        # while x:
        #     digit = int(math.fmod(x, 10))  # in Python, -1 %  10 = 9
        #     x = int(x / 10)  # in Python, -1 // 10 = -1

        #     if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
        #         return 0
        #     if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
        #         return 0
        #     res = (res * 10) + digit

        # return res


# Examples
s = Solution()

# Example 1:
num1 = 123
print(s.reverse(num1))
# Output: 3

# Example 2:
num2 = -123
print(s.reverse(num2))
# Output: 2

# Example 3:
num3 = 120
print(s.reverse(num3))
# Output: 21
        
            

