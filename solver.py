def evaluate_postfix(tokens):
    """evaluate expression written in postfix notation, returns a number.
    tokens should be an iterable of strings (operators and numbers)"""
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "x":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)

    return stack.pop()


def shunting_yard(tokens):
    """transform infix (normal) expression notation to postfix notation.
    tokens should be an iterable of strings (operators and numbers)"""
    queue = []
    stack = []
    for token in tokens:
        if token.isdigit():
            queue.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while len(stack) > 0 and stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop()
        else:
            if token == "*" or token == "/":
                while len(stack) > 0 and (stack[-1] == "x" or stack[-1] == "/"):
                    queue.append(stack.pop())
            elif token == "+" or token == "-":
                while len(stack) > 0 and (stack[-1] == "x" or stack[-1] == "/" or stack[-1] == "+" or stack[-1] == "-"):
                    queue.append(stack.pop())
            stack.append(token)

    while len(stack) > 0:
        queue.append(stack.pop())

    return queue


def solve(expression):
    """receive expression in form of string, parse it, and calculate the result,
    expression should have spaces between tokens"""
    infix_tokens = expression.split(" ")
    postfix_tokens = shunting_yard(infix_tokens)
    return evaluate_postfix(postfix_tokens)
