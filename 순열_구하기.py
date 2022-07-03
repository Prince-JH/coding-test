def DFS(L, n, m):
    if L == m:
        res.append(sub_res[:])
    else:
        for i in range(0, n):
            if temp[i] == 0:
                temp[i] = 1
                sub_res[L] = i + 1
                DFS(L + 1, n, m)
                temp[i] = 0


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    n, m = 3, 3
    temp = [0] * m
    sub_res = [0] * m
    res = list()
    DFS(0, n, m)
    print(res)

