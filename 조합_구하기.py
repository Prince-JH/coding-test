def DFS(L, n, m, num):
    if L == m:
        res.append(sub_res[:])
    else:
        for i in range(num, n):
            if temp[i] == 0:
                temp[i] = 1
                sub_res[L] = i + 1
                DFS(L + 1, n, m, i + 1)
                temp[i] = 0


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    n, m = 7, 4
    temp = [0] * n
    res = list()
    sub_res = [0] * m
    DFS(0, n, m, 0)
    print(res)
    print(len(res))
