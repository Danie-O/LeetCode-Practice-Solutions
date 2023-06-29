import sys

class Solution:

    # Using monotonic stack
    # TIME: O(N), SPACE: O(N)
    def removeKdigits(self, num: str, k: int) -> str:
        # Increase the limit for integer string conversion
        # sys.set_int_max_str_digits(90001)

        stack = []

        for char in num:
            while k > 0 and stack and stack[-1] > char:
                k -= 1
                stack.pop()
            if stack or char != "0":
                stack.append(char)

        # if k is still not zero (the input string is an increasing monotonic string)
        stack = stack[:len(stack) - k]
        result = "".join(stack)
        return result if result else "0"
            
            

        
