import sys


def DFS(L, n, f):
    if len(res) > 0:
        return
    elif L == n:
        total = 0
        # print(sub_res, comb)
        for i in range(n):
            total += sub_res[i] * comb[i]
        if total == f:
            res.append(sub_res[:])
    else:
        for i in range(0, n):
            if temp[i] == 0:
                temp[i] = 1
                sub_res[L] = i + 1
                DFS(L + 1, n, f)
                temp[i] = 0


def get_combination(length):
    _list = [1] * length
    for i in range(1, length):
        _list[i] = _list[i - 1] * (length - i) / i
    return _list


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    n, f = 10, 2196
    comb = get_combination(n)
    temp = [0] * n
    sub_res = [0] * n
    res = list()
    DFS(0, n, f)
    print(res)
