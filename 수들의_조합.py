def DFS(L, n, m, num, k):
    if L == m:
        if sum(sub_res) % k == 0:
            res.append(sub_res[:])
    else:
        for i in range(num, n):
            if temp[i] == 0:
                temp[i] = 1
                sub_res[L] = nums[i]
                DFS(L + 1, n, m, i + 1, k)
                temp[i] = 0


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    nums = [2, 4, 5, 8, 12]
    n, m, k = 5, 3, 6
    temp = [0] * n
    res = list()
    sub_res = [0] * m
    DFS(0, n, m, 0, k)
    print(res)
    print(len(res))
