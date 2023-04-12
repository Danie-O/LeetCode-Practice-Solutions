class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        isNeg = 0 # assume number is positive (not negative)
        # x_dup = x

        if x == 0:
            return x
        elif x < 0:
            x = abs(x)
            isNeg = 1  # change value of isNeg since x is negative
        
        while x:
            temp = x % 10
            res = res * 10 + temp 
            x = x // 10

        if -2**31 <= res <= 2**31: # check if number is within given range
            if isNeg:
                return -res
            else:
                return res
                # return (x_dup // abs(x_dup)) * res
        else:
            return 0

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
        
            

