


def DFS(n):
    left = list()
    right = list()
    if len(flag) > 0:
        return
    if n == cnt:
        for i in range(cnt):
            if res[i] == 1:
                left.append(nums[i])
            else:
                right.append(nums[i])
        # print('left:', left)
        # print('right:', right)
        if sum(left) == sum(right):
            print('YES')
            flag.append(1)
    else:
        res[n] = 1
        DFS(n + 1)
        res[n] = 0
        DFS(n + 1)


if __name__ == '__main__':
    # main script 에 생성되면 전역변수
    cnt = 6
    nums = [3, 6, 13, 11, 7, 16, 34, 23, 12]
    res = [0] * 6
    flag = list()
    DFS(0)
    if len(flag) < 1:
        print('NO')
