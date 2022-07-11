if __name__ == '__main__':
    records = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 9
    left, right = max(records), sum(records)

    while left <= right:
        mid = (left + right) // 2
        cnt = 1
        temp = mid
        for record in records:
            if temp >= record:
                temp -= record
            else:
                temp = mid - record
                cnt += 1
        if cnt > n:
            left = mid + 1
        else:
            res = mid
            right = mid - 1

    print(res)
