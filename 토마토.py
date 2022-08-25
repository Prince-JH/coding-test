from collections import deque

if __name__ == '__main__':
    board = [
        [0, -1, 0, -1, 1, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, -1, 0, -1],
        [1, 0, 0, 0, -1, 0, 1, -1, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, -1, 0],
        [-1, 0, 0, 0, -1, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 1, 0, 0]
    ]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(board)
    m = len(board[0])
    res = list()
    cnt = 0
    queue = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                queue.append((i, j))
                board[i][j] = -1
    while True:
        while queue:
            temp = queue.popleft()
            board[temp[0]][temp[1]] = -1
            for k in range(4):
                x = temp[0] + dx[k]
                y = temp[1] + dy[k]
                if 0 <= x < n and 0 <= y < m and board[x][y] == 0:
                    board[x][y] = 1
                    # queue.append((x, y))
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    queue.append((i, j))
                    board[i][j] = -1
        if queue:
            cnt += 1
        else:
            break

    if any(0 in x for x in board):
        print(-1)
    print(cnt)
