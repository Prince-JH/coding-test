import sys
from collections import deque


def DFS(L, n, start, current):
    if L == n - 1:
        if board[current[0]][current[1]] == 2:
            print('!!!END!!!', start)
            sys.exit()
    else:
        for i in range(3):
            board[current[0]][current[1]] = 0
            x = current[1] + dx[i]
            y = current[0] + dy[i]
            if 0 <= y < n and 0 <= x < n and board[y][x] >= 1:
                if dy[i] == 1:
                    L += 1
                DFS(L, n, start, (y, x))
                board[y][x] = 1
                break


if __name__ == '__main__':
    n = 10
    board = [[] for _ in range(10)]
    f = open("/Users/jihoon/Downloads/pythonalgorithm_formac/섹션 7/16. 사다리타기/in5.txt", 'r')
    for i in range(10):
        line = f.readline()
        board[i] = list(map(int, line.split()))
    f.close()
    dx = [-1, 1, 0]
    dy = [0, 0, 1]
    for i in range(n):
        if board[0][i] == 1:
            DFS(0, n, i, (0, i))
