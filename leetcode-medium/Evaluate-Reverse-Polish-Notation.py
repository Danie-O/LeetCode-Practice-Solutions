class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
           - create array of operators & stack to store integers(operands)
           - for each element in 'tokens', 
                - if operator: pop last two items in stack & apply operator
                  (make result an int for division truncation toward 0)
                    - assign result to result var & append result to stack 
                - if operand: append int(operand) to stack
        """
        # For both solutions;
        # TIME: O(n) => we go through all items in the input array(n number of items)
        # SPACE: O(n) => the space required by the stack grows linearly with the no of tokens in input

        # operators = ["+", "-", "/", "*"]
        # stack = []
        # res = 0

        # if len(tokens) <= 1:
        #     return int(tokens[0])

        # for i in tokens:
        #     if i in operators:
        #         b = stack.pop()
        #         a = stack.pop()
        #         if i == "+":
        #             res = a + b
        #         elif i == "-":
        #             res = a - b
        #         elif i == "/":
        #             res = int(a / b)
        #         elif i == "*":
        #             res = int(a * b)
        #         stack.append(res)
        #     else:
        #         stack.append(int(i))
        # return stack[0]


        # STORING OPERATORS AND OPERATIONS WITH A DICT
        res = 0
        stack = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                operation = operators[token]
                res = operation(a, b)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]
