def DFS(v, n, score_sum):
    if v == n:
        if score_sum > res[0]:
            res[0] = score_sum
    else:
        DFS(v + _input[v][0], n, score_sum + _input[v][1])
        DFS(v + 1, n, score_sum)


if __name__ == '__main__':
    _input = [(3, 20), (2, 15), (3, 50), (3, 25), (2, 20), (2, 30), (1, 10)]
    res = [0]
    DFS(0, len(_input), 0)
    print(res)
