def DFS_pick(L, n, m):
    print(L, n, m)
    if L == m:
        temp.append(res[:])
    else:
        for i in range(0, n):
            res[L] = i + 1
            DFS_pick(L + 1, n, m)


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    n, m = 3, 2
    temp = list()
    res = [0] * m
    DFS_pick(0, n, m)
    print(temp)
