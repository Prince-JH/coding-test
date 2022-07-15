if __name__ == '__main__':
    times = [(1, 4), (3, 5), (4, 6), (5, 7), (2, 3)]
    n = 5
    times.sort(key=lambda x: (x[1]))
    res = list()
    for time in times:
        start = time[0]
        if len(res) == 0:
            res.append(time)
        else:
            if start >= res[-1][1]:
                res.append(time)

    print(len(res))
