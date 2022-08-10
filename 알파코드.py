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
            print(nums[L: i + 1])
            if n[L] != '0' and 65 <= int(nums[L: i + 1]) + 64 <= 90:
                res.append(chr(int(nums[L: i + 1]) + 64))
                DFS(i + 1)
                res.pop()


if __name__ == '__main__':
    nums = '25114'
    n = len(nums)
    temp = list()
    res = list()
    DFS(0, n)
    print(res)
