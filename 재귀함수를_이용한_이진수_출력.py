def DFS(num, res):
    if num <= 1:
        res = str(num) + res
        print(res)
    else:
        res = str(num % 2) + res
        num = num // 2
        DFS(num, res)


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    num = 11
    res = ''
    DFS(num, res)
