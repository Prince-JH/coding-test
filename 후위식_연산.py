if __name__ == '__main__':
    expression = list('352+*9-')
    stack = list()
    res = 0
    for e in expression:
        if e.isdigit():
            stack.append(e)
        elif e == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif e == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif e == '-':
            stack.append(-(int(stack.pop()) - int(stack.pop())))
        elif e == '/':
            stack.append(int(stack.pop()) / int(stack.pop()))

    print(stack[0])
