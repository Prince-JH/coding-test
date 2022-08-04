def DFS(v, n):
    if v == n:
        temp = 0
        for i in range(len(ch)):
            if ch[i] == 1:
                temp += weights[i]
            elif ch[i] == -1:
                temp -= weights[i]
        res.add(temp)
    else:
        ch[v] = 1
        DFS(v + 1, n)
        ch[v] = 0
        DFS(v + 1, n)
        ch[v] = -1
        DFS(v + 1, n)


if __name__ == '__main__':
    weights = [1152, 835, 1351, 21351, 21353, 5533, 8359, 10350, 101, 108]
    ch = [0] * len(weights)
    nums = [i for i in range(1, sum(weights) + 1)]
    res = set()
    # print(nums)
    DFS(0, len(weights))
    print(len(set(nums) - set(res)))
