if __name__ == '__main__':
    coordinates = [1, 2, 8, 4, 9]
    n = 3
    coordinates.sort()
    left, right = coordinates[0], coordinates[-1] - coordinates[0]

    while left <= right:
        mid = (left + right) // 2

        cnt = 1
        last = coordinates[0]
        for i in range(1, len(coordinates)):
            if coordinates[i] - last >= mid:
                last = coordinates[i]
                cnt += 1
        if cnt >= n:
            left = mid + 1
            res = mid
        else:
            right = mid - 1

    print(res)
