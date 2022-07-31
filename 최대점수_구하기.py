def DFS(v, n, time_limit, score_sum, time_sum):
    if time_sum > time_limit:
        return
    elif v == n:
        if score_sum > res[0]:
            res[0] = score_sum
    else:
        DFS(v + 1, n, time_limit, score_sum + _input[v][0], time_sum + _input[v][1])
        DFS(v + 1, n, time_limit, score_sum, time_sum)

if __name__ == '__main__':
    _input = [(10, 5), (25, 12), (15, 8), (6, 3), (7, 4)]
    time_limit = 20
    res = [0]
    DFS(0, len(_input), time_limit, 0, 0)
    print(res)
