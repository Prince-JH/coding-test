import sys
def DFS(v, n):
    if v == n - 1:
        for p in path:
            print(p, end=' ')
        print()
    else:
        for i in range(n):
            if matrix[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                # print('ch:', ch)
                path.append(i + 1)
                DFS(i, n)
                ch[i] = 0
                path.pop()

if __name__ == '__main__':
    n = 5
    matrix = [[0] * n for i in range(n)]
    _input = [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 5], [3, 4], [4, 2], [4, 5]]
    for i in _input:
        matrix[i[0] - 1][i[1] - 1] = 1
    print(matrix)
    path = [1]
    ch = [0] * n
    ch[0] = 1
    DFS(0, n)

