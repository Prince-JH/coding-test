def DFS(v, n, a_total, b_total, c_total):
    global _min
    # print(v, a_total, b_total, c_total)
    if v == n:
        if a_total != b_total and b_total != c_total and a_total != c_total:
            temp = max(a_total, b_total, c_total) - min(a_total, b_total, c_total)
            if _min > temp:
                print(a_total, b_total, c_total)
                _min = temp
    else:
        DFS(v + 1, n, a_total + coins[v], b_total, c_total)
        DFS(v + 1, n, a_total, b_total + coins[v], c_total)
        DFS(v + 1, n, a_total, b_total, c_total + coins[v])


if __name__ == '__main__':
    coins = [8, 9, 11, 12, 23, 15, 17]
    a_total = b_total = c_total = 0
    _min = max(coins)
    print(sum(coins))
    n = len(coins)
    # print(nums)
    DFS(0, n, a_total, b_total, c_total)
    print(_min)
