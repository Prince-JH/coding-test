import sys
from collections import deque


def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for j in range(len(houses)):
            x1 = houses[j][0]
            y1 = houses[j][1]
            dis = float("inf")
            for k in combinations:
                x2 = pizzas[k][0]
                y2 = pizzas[k][1]
                dis = min(dis, abs(x1 - x2) + abs(y1 - y2))
            sum += dis
        if sum < res:
            res = sum
    else:
        for i in range(s, len(pizzas)):
            combinations[L] = i
            DFS(L + 1, i + 1)


if __name__ == '__main__':
    f = open("/Users/jihoon/Downloads/pythonalgorithm_formac/섹션 7/17. 피자 배달 거리/in2.txt", 'r')
    n, m = map(int, f.readline().split())
    board = [[] for _ in range(n)]
    for i in range(n):
        line = f.readline()
        board[i] = list(map(int, line.split()))
    f.close()
    houses = list()
    pizzas = list()
    combinations = [0] * m
    res = float("inf")
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                houses.append((i, j))
            elif board[i][j] == 2:
                pizzas.append((i, j))

    DFS(0, 0)
    print(res)