def DFS(n):
    print(n)
    if n < 0:
        return
    elif n == 0:
        for i in range(len(ch)):
            res.append(ch[:])
    else:
        for i in range(len(coins)):
            if ch[i] < coins[i][1]:
                ch[i] += 1
                n -= coins[i][0]
                DFS(n)
                ch[i] -= 1
                n += coins[i][0]
            DFS(n)


if __name__ == '__main__':
    amount = 20
    coins = [(5, 3), (10, 2), (1, 5)]
    ch = [0] * len(coins)
    res = list()
    # print(nums)
    DFS(amount)
