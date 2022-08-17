def DFS(L, n, x, y):
    global cnt
    # print(x, y)
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # print('x, y', x, y)
            if 0 <= new_x < n and 0 <= new_y < n and maze[new_x][new_y] == 0:
                maze[x][y] = 1  # 한 번 지난 곳은 벽으로 만들어버려서 가지 못하도록
                DFS(L + 1, n, new_x, new_y)
                maze[x][y] = 0


if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0]]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    n = len(maze)
    maze[0][0] = 1
    DFS(0, n, 0, 0)
    print(cnt)
