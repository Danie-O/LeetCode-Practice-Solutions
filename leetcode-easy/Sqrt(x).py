""" PROMPT: Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
    
    The returned integer should be non-negative as well. You must not use any built-in exponent function or operator.
    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        i = 1
        square = i * i
        while x >= square:
            i += 1
            square = i * i

        return i - 1    # round down i to nearest integer

        # using binary search approach(O(log n))
        # left = 0
        # right = x

        # while middle:
        #     middle = (left + right) // 2
        #     if (middle * middle) == x:
        #         return middle
        #     else if (middle * middle) < x:
        #         left = middle + 1
        #     else if (middle * middle) > x:
        #         right = middle - 1

        # return middle


# Examples
example = Solution()

# Example 1:
x = 49
print(example.mySqrt(x))
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
