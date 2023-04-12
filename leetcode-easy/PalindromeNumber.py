""" PROMPT:
    Given an integer x, return true if x is a palindrome and false otherwise.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # helper function to reverse x
        def reverse_num(num):
            res = 0
            while num:
                mod = num % 10
                res = (res * 10) + mod
                num = num // 10
            return res

        # if x is negative, it's not a palindrome so return it immediately
        if x < 0:
            return False
        # check if the reverse of x is equal to x
        elif reverse_num(x) == x:
            return True
        else:
            return False
        
        
# Examples
s = Solution()

# Example 1:
num1 = 121
print(s.isPalindrome(num1))
# Output: true

# Example 2:
num2 = -121
print(s.isPalindrome(num2))
# Output: false

# Example 3:
num3 = 10
print(s.isPalindrome(num3))
# Output: false