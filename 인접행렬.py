import sys

if __name__ == '__main__':
    n = 6
    matrix = [[0] * n for _ in range(n)]
    print(matrix)

    _input = [[1, 2, 7], [1, 3, 4], [2, 1, 2], [2, 3, 5], [2, 5, 5], [3, 4, 5], [4, 2, 2], [4, 5, 5], [6, 4, 5]]
    for i in _input:
        matrix[i[0] - 1][i[1] - 1] = i[2]

    print(matrix)
