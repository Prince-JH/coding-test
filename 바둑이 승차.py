


def DFS(n, total):
    if total > _max:
        return
    elif n == cnt:
        res.append(total)
    else:
        DFS(n + 1, total + nums[n])
        DFS(n + 1, total)


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    cnt = 5
    _max = 259
    nums = [81, 58, 42, 33, 61]
    res = list()
    DFS(0, 0)
    print(res)
    print(max(res))
