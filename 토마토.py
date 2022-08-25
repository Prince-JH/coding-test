from collections import deque

if __name__ == '__main__':
    board = [[0, 0, -1, 0, 0, 0],
             [0, 0, 1, 0, -1, 0],
             [0, 0, -1, 0, 0, 0],
             [0, 0, 0, 0, -1, 1]]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(board)
    m = len(board[0])
    res = list()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queue = deque()
                queue.append((i, j))
                board[i][j] = -1
                while queue:
                    print(queue)
                    for b in board:
                        print(b)
                    temp = queue.popleft()
                    board[temp[0]][temp[1]] = -1
                    for k in range(4):
                        x = temp[0] + dx[k]
                        y = temp[1] + dy[k]
                        if 0 <= x < n and 0 <= y < m and board[x][y] == 0:
                            board[x][y] = 1
                            queue.append((x, y))
                    cnt += 1

    print(cnt)
