


def DFS(n, total, check_total):
    global res
    if sum_nums - check_total + total < res:
        return
    elif total > _max:
        return
    elif n == cnt:
        if total > res:
            res = total
    else:
        DFS(n + 1, total + nums[n], check_total + nums[n])
        DFS(n + 1, total, check_total + nums[n])


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    cnt = 5
    _max = 259
    nums = [81, 58, 42, 33, 61]
    sum_nums = sum(nums)
    res = 0
    DFS(0, 0, 0)
    print(res)
