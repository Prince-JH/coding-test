if __name__ == '__main__':
    houses = [[0, 1, 1, 0, 1, 0, 0],
              [0, 1, 1, 0, 1, 0, 1],
              [1, 1, 1, 0, 1, 0, 1],
              [0, 0, 0, 0, 1, 1, 1],
              [0, 1, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 0],
              [0, 1, 1, 1, 0, 0, 0]]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(houses)
    ch = [[0] * n for _ in range(n)]
    res = list()
    for i in range(n):
        for j in range(n):
            if houses[i][j] == 1:
                queue = list()
                cnt = 1
                queue.append((i, j))
                houses[i][j] = 0
                while queue:
                    temp = queue.pop(0)
                    for k in range(4):
                        x = temp[0] + dx[k]
                        y = temp[1] + dy[k]
                        if 0 <= x < n and 0 <= y < n and houses[x][y] == 1:
                            houses[x][y] = 0
                            cnt += 1
                            queue.append((x, y))
                res.append(cnt)

    print(res)
