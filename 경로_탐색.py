import sys
def DFS(v, n):
    global cnt
    if v == n - 1:
        cnt += 1
        for p in path:
            print(p, end=' ')
        print()
    else:
        for i in range(n):
            if matrix[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i + 1)
                DFS(i, n)
                path.pop()
                ch[i] = 0


if __name__ == '__main__':
    n = 5
    matrix = [[0] * n for _ in range(n)]
    ch = [0] * n

    _input = [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 5], [3, 4], [4, 2], [4, 5]]
    for i in _input:
        matrix[i[0] - 1][i[1] - 1] = 1

    path = [1]
    cnt = 0
    ch[0] = 1
    DFS(0, n)
    print(cnt)
