def validParentheses(s: str):
    stack = []
    brackets = {'(':')', '{': '}', '[': ']'}

    for char in s:
        if char in brackets:
            stack.append(char)
        elif stack == [] or brackets[stack.pop()] != char:
           return False
        """ Note for elif statement above:
        
            If the stack is empty, the close bracket does not have a open bracket before it
            Also, if the last bracket in the stack is not the corresponding open bracket of the current
            character, the input string is invalid
        """
    # check if any opening brackets do not have corresponding closing brackets
    return stack == []

print(validParentheses("(())("))
print(validParentheses("([])"))
print(validParentheses("([)]"))
