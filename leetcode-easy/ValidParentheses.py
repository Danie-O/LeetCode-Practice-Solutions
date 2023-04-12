"""PROMPT:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_to_close = {"(":")", "{":"}", "[":"]"}
        for character in s:
            if character in open_to_close.keys():  
                # If the current character is an open bracket, add to stack
                stack.append(character)
            elif stack==[] or character!=open_to_close[stack.pop()]: 
                return False
            """ Note for elif statement above:
                If the stack is empty, the close bracket does not have a open bracket before it
                Also, if the last bracket in the stack is not the corresponding open bracket of the current
                character, the input string is invalid
            """        
        # if not empty, there are some unclosed open brackets - string is invalid
        return stack == []  


# Examples
s = Solution()

# Example 1:
str1 = "()"
print(s.isValid(str1))
# Output: true

# Example 2:
str2 = "()[]{}"
print(s.isValid(str2))
# Output: true

# Example 3:
str3 = "(]"
print(s.isValid(str3))
# Output: false


