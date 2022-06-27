def DFS(L, n, total, cnt):
    global res
    if total < 0:
        return
    elif total == 0:
        if cnt < res:
            res = cnt
    elif cnt > res:
        return
    else:
        for i in range(0, n):
            DFS(L + 1, n, total - coins[i], cnt + 1)


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    coins = [1, 5, 10, 15, 20, 25, 30, 50, 70, 65, 90, 100]
    total = 290
    coins.sort(reverse=True)
    res = float("inf")
    DFS(0, len(coins), total, 0)
    print(res)
