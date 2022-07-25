import sys


def DFS(L, nums, temp):
    if L == len(nums):
        left, right = 0, 0
        for i in range(len(nums)):
            if temp[i] == 1:
                left += nums[i]
            else:
                right += nums[i]
        if left == right:
            print('YES')
            sys.exit()
    else:
        temp[L] = 1
        DFS(L + 1, nums, temp)
        temp[L] = 0
        DFS(L + 1, nums, temp)

if __name__ == '__main__':
    nums = [3, 6, 13, 11, 7, 16, 34, 23, 12]
    temp = [0] * len(nums)
    DFS(0, nums, temp)
    print('NO')