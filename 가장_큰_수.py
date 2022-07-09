if __name__ == '__main__':
    num = '5276823'
    n = 3
    cnt = 0
    stack = list()
    stack.append(num[0])

    for i in range(1, len(num)):
        while len(stack) > 0 and stack[-1] < num[i] and cnt < n:
            stack.pop()
            cnt += 1
        stack.append(num[i])

    print(stack)
    print(''.join(stack))
