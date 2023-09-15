def reversePolishNotation(tokens: str):
    if len(tokens) <= 1: return int(tokens[0])

    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b)
    }

    # stack to keep track of seen operands
    stack = []

    for char in tokens:
        if char in operators:
            op2 = int(stack.pop())
            op1 = int(stack.pop())
            operation = operators[char]
            res = operation(op1, y)
            stack.append(res)
        else:
            stack.append(int(char))
    return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(reversePolishNotation(tokens))