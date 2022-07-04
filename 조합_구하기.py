def DFS(L, n, m):
    if L == m:
        print(temp)
        res.append(temp)
    else:
        for i in range(0, n):
            if temp[L] == 0:
                temp[L] = i + 1
                DFS(L + 1, n, m)
                temp[L] = 0


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    n, m = 4, 2
    temp = [0] * m
    res = list()
    DFS(0, n, m)
    print(res)
    print(len(res))
