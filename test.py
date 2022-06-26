import asyncio
from datetime import datetime

layout = {
    'H': (1, 1), 'A': (0, 0), 'P': (2, 3), 'Y': (4, 0)
}


def temp(word):
    answer = 0
    cnt = len(word)
    res = list()
    left = word[0]
    right = None
    DFS(0, cnt, 0, word, res, left, right)
    print(res)
    answer = min(res)
    print(answer)


def get_dist(a, b):
    pos_a = layout[a]
    pos_b = layout[b]
    dist = abs(pos_b[0] - pos_a[0]) + abs(pos_b[1] - pos_a[1])
    return dist


def DFS(n, cnt, total, word, res, left, right):
    if len(res) > 0 and total > res[-1]:
        return
    elif n == len(word) - 1:
        if len(res) == 0:
            res.append(total)
        elif total < res[-1]:
            res.append(total)
    else:
        DFS(n + 1, cnt, total + get_dist(left, word[n + 1]), word, res, word[n + 1], right)
        if right is None:
            right = word[n + 1]
        DFS(n + 1, cnt, total + get_dist(right, word[n + 1]), word, res, left, word[n + 1])


if __name__ == '__main__':
    temp("HAPPY")
