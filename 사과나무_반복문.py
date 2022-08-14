if __name__ == '__main__':
    orchard = [[74, 10, 31, 26, 59, 16, 89],
               [78, 44, 49, 1, 64, 33, 15],
               [9, 95, 70, 18, 22, 25, 40],
               [62, 77, 28, 3, 78, 75, 23],
               [82, 38, 20, 16, 42, 1, 79],
               [1, 24, 2, 25, 95, 26, 79],
               [4, 35, 46, 94, 70, 44, 83]]
    cnt = 0

    for i in range(len(orchard)):
        if i <= len(orchard) // 2:
            for j in range(len(orchard) // 2 - i, len(orchard) // 2 + i + 1):
                cnt += orchard[i][j]
        else:
            for j in range(i - len(orchard) // 2, len(orchard) // 2 - i + len(orchard)):
                cnt += orchard[i][j]

    print(cnt)

1, 3
2, 2
