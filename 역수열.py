if __name__ == '__main__':
    seq = '53402110'
    seq = list(map(int, seq))
    length = len(seq)
    res = [0] * length
    res[seq[0]] = 1
    last = None

    for i in range(1, length):
        if seq[i] != 0:
            index = 0
            cnt = 0
            while True:
                if cnt == seq[i] and res[index] == 0:
                    res[index] = i + 1
                    break
                if res[index] > i + 1 or res[index] == 0:
                    cnt += 1
                index += 1
        else:
            res[res.index(0)] = i + 1

    print('res:', res)
