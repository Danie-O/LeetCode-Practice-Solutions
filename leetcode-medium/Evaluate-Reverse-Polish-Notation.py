class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
           - store operators in an array 
           - create stack to store integers(operands)
           - for each element in input, 
                - if operator: pop last two items in stack & apply operator
                  (make result an int for division truncation toward 0)
                    - assign result to result var & append result to stack 
                - if operand: append int(operand) to stack
        """
        operators = ["+", "-", "/", "*"]
        stack = []
        res = 0

        if len(tokens) <= 1:
            return int(tokens[0])

        for i in tokens:
            if i in operators:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    res = a + b
                elif i == "-":
                    res = a - b
                elif i == "/":
                    res = int(a / b)
                elif i == "*":
                    res = int(a * b)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]
