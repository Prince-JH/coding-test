def DFS(L, n, cur):
    if L == n:
        temp.append(res[:])
    else:
        for i in range(0, n):
            if i + 1 != cur:
                res[L] = i + 1
                DFS(L + 1, n, i + 1)


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    n, m = 4, 16
    temp = list()
    res = [0] * n
    DFS(0, n, 0)
    print(temp)

