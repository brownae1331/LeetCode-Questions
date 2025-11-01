def evalRPN(tokens: list[str]) -> int:
    stack = []
    operators = {
        "+" : lambda a, b : a + b,
        "-" : lambda a, b : a - b,
        "*" : lambda a, b : a * b,
        "/" : lambda a, b : a / b
        }
    for token in tokens:
        if token in operators:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(int(operators[token](num1, num2)))
        else:
            stack.append(int(token))
    return stack[-1]

if __name__ == "__main__":
    output = evalRPN(tokens=["0", "3", "/"])
    print(output)