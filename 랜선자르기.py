if __name__ == '__main__':
    nums = [802, 743, 457, 539]
    n = 11
    left, right = 1, max(nums)

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for num in nums:
            cnt += num // mid
        if cnt >= n:
            res = mid
            left = mid + 1
        else:
            right = mid - 1

    print(res)
