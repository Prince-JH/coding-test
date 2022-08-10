def DFS(L, n):
    global cnt
    if L == n:
        for x in res:
            print(x, end='')
        print()
        cnt += 1
        return
    else:
        for i in range(L, n):
            # print(nums[L: i + 1])
            if nums[L] != '0' and 1 <= int(nums[L: i + 1]) <= 26:
                res.append(chr(int(nums[L: i + 1]) + 64))
                DFS(i + 1, n)
                res.pop()


if __name__ == '__main__':
    cnt = 0
    nums = '115213102'
    n = len(nums)
    temp = list()
    res = list()
    DFS(0, n)
    print(cnt)
