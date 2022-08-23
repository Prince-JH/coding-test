from collections import deque

if __name__ == '__main__':
    board = [[1, 1, 0, 0, 0, 1, 0],
             [0, 1, 1, 0, 1, 1, 0],
             [0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 1, 1],
             [1, 1, 0, 1, 1, 0, 0],
             [1, 0, 0, 0, 1, 0, 0],
             [1, 0, 1, 0, 1, 0, 0]]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    n = len(board)
    res = list()
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queue = deque()
                queue.append((i, j))
                board[i][j] = 0
                while queue:
                    # print(queue)
                    temp = queue.popleft()
                    for k in range(8):
                        x = temp[0] + dx[k]
                        y = temp[1] + dy[k]
                        if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                            board[x][y] = 0
                            queue.append((x, y))
                res.append('')

    print(len(res))
