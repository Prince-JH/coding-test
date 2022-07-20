if __name__ == '__main__':
    expression = list('5+8+6*5-(3+2)-7*3-5+(3+2*3)+(5+3+2-5*2)+3')
    stack = list()
    res = ''
    for i in range(len(expression)):
        if expression[i].isdigit():
            res += expression[i]
            if stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
        elif expression[i] == ')':
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()
            res += stack.pop()
        elif expression[i] == '+' or expression[i] == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(expression[i])
        else:
            stack.append(expression[i])

    while stack:
        res += stack.pop()

    print(res)
