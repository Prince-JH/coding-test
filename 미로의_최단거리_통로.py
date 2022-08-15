if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 1, 0, 1, 1],
            [1, 1, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 0]]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = list()
    n = len(maze)
    dis = [[-1] * n for _ in range(n)]
    dis[0][0] = 0
    queue.append((0, 0))
    res = list()

    while queue:
        # print(queue)
        size = len(queue)
        for i in range(size):
            temp = queue.pop(0)
            temp_dis = dis[temp[0]][temp[1]]
            for j in range(4):
                x = temp[0] + dx[j]
                y = temp[1] + dy[j]
                if 0 <= x < n and 0 <= y < n and maze[x][y] == 0:
                    maze[x][y] = 1 # 한 번 지난 곳은 벽으로 만들어버려서 가지 못하도록
                    dis[x][y] = temp_dis + 1
                    queue.append((x, y))
        # print(size)
    for x in dis:
        print(x)

