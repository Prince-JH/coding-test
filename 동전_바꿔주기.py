def DFS(v, n, amount):
    if amount < 0:
        return
    elif amount == 0:
        res.append(0)
    elif v == n:
        return
    else:
        for i in range(coins[v][1] + 1):
            DFS(v + 1, n, amount - coins[v][0] * i)
                # ch[i] -= 1
                # amount += coins[i][0]
                # DFS(v + 1, n, amount)


if __name__ == '__main__':
    amount = 486
    coins = [(1, 10), (3, 9), (7, 9), (12, 7), (13, 9), (25, 7), (47, 5)]
    n = len(coins)
    ch = [0] * len(coins)
    res = list()
    # print(nums)
    DFS(0, n, amount)
    print(len(res))