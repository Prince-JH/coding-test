def DFS(start, end):
    global cnt
    # print(x, y)
    if start == end:
        cnt += 1
    else:
        for i in range(4):
            new_x = start[0] + dx[i]
            new_y = start[1] + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and mountain[new_x][new_y] >= mountain[start[0]][start[1]]:
                DFS((new_x, new_y), end)


if __name__ == '__main__':
    mountain = [[2, 23, 92, 78, 93],
                [59, 50, 48, 90, 80],
                [30, 53, 70, 75, 96],
                [94, 91, 82, 89, 93],
                [97, 98, 95, 96, 100]]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    n = len(mountain)
    _min = min(map(min, mountain))
    _max = max(map(max, mountain))
    for i in range(len(mountain)):
        for j in range(len(mountain)):
            if mountain[i][j] == _min:
                start = (i, j)
            if mountain[i][j] == _max:
                end = (i, j)
    mountain[start[0]][start[1]] = 1
    DFS(start, end)
    print(cnt)
