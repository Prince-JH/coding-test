if __name__ == '__main__':
    stack = list()
    inp = list('(((()(()()))(())()))(()())(((()(()()))(())()))(()())(((()())))')
    res = 0

    for i in range(len(inp)):
        if inp[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if inp[i - 1] == '(':
                res += len(stack)
            else:
                res += 1
    print(res)
