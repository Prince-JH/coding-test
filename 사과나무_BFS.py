if __name__ == '__main__':
    orchard = [[74, 10, 31, 26, 59, 16, 89],
               [78, 44, 49, 1, 64, 33, 15],
               [9, 95, 70, 18, 22, 25, 40],
               [62, 77, 28, 3, 78, 75, 23],
               [82, 38, 20, 16, 42, 1, 79],
               [1, 24, 2, 25, 95, 26, 79],
               [4, 35, 46, 94, 70, 44, 83]]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = list()
    n = len(orchard)
    ch = [[0] * n for _ in range(n)]
    queue.append((n // 2, n // 2))
    ch[n // 2][n // 2] = 1
    cnt = 0
    cnt += orchard[n // 2][n // 2]
    L = 0

    while queue:
        if L == n // 2:
            break
        size = len(queue)
        for i in range(size):
            temp = queue.pop(0)
            for j in range(4):
                x = temp[0] + dx[j]
                y = temp[1] + dy[j]
                if ch[x][y] == 0:
                    cnt += orchard[x][y]
                    ch[x][y] = 1
                    queue.append((x, y))
        # print(L, size)
        # for x in ch:
        #     print(x)
        L += 1

    print(cnt)
