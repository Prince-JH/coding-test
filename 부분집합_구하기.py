def DFS(L, num, res):
    if L == num:
        for i in range(len(res)):
            if res[i] == 1:
                print(i + 1, end=' ')
        print()
    else:
        res[L] = 1
        DFS(L + 1, num, res)
        res[L] = 0
        DFS(L + 1, num, res)


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    num = 5
    res = [0] * num
    DFS(0, num, res)
