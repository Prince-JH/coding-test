if __name__ == '__main__':
    areas = [[6, 8, 2, 6, 2],
             [3, 2, 3, 4, 6],
             [6, 7, 3, 3, 2],
             [7, 2, 5, 3, 6],
             [8, 9, 5, 2, 7]]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(areas)
    res = list()
    for i in range(max(map(max, areas))):
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for j in range(n):
            for k in range(n):
                if areas[j][k] > i and ch[j][k] == 0:
                    queue = list()
                    queue.append((j, k))
                    ch[j][k] = 1
                    cnt += 1
                    while queue:
                        # print(i, queue)
                        temp = queue.pop(0)
                        for l in range(4):
                            x = temp[0] + dx[l]
                            y = temp[1] + dy[l]
                            if 0 <= x < n and 0 <= y < n and areas[x][y] > i and ch[x][y] == 0:
                                ch[x][y] = 1
                                queue.append((x, y))
        res.append(cnt)

    print(res)
