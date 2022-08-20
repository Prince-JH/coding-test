def DFS(x, y):
    global cnt
    cnt += 1
    houses[x][y] = 0
    for k in range(4):
        new_x = x + dx[k]
        new_y = y + dy[k]
        if 0 <= new_x < n and 0 <= new_y < n and houses[new_x][new_y] == 1:
            DFS(new_x, new_y)


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
    res = list()
    for i in range(n):
        for j in range(n):
            if houses[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)

    print(res)
