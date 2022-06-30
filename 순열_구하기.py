def DFS_pick(L, n, m, cur):
    print(L, n, m)
    print(res)
    if L == m:
        temp.append(res[:])
    else:
        for i in range(0, n):
            if i + 1 != cur:
                res[L] = i + 1
                DFS_pick(L + 1, n, m, i + 1)


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    n, m = 3, 2
    temp = list()
    res = [0] * m
    DFS_pick(0, n, m, 0)
    print(temp)
    print(len(temp))
