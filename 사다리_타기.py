import sys
from collections import deque


def DFS(y, x):
    if y == 0:
        print('!!!END!!!', x)
        sys.exit()
    else:
        for i in range(3):
            board[y][x] = 0
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= yy < n and 0 <= xx < n and board[yy][xx] >= 1:
                DFS(yy, xx)
                board[y][x] = 1
                break


if __name__ == '__main__':
    n = 10
    board = [[] for _ in range(10)]
    f = open("/Users/jihoon/Downloads/pythonalgorithm_formac/섹션 7/16. 사다리타기/in2.txt", 'r')
    for i in range(10):
        line = f.readline()
        board[i] = list(map(int, line.split()))
    f.close()
    dx = [-1, 1, 0]
    dy = [0, 0, -1]
    for i in range(n):
        if board[9][i] == 2:
            DFS(9, i)
