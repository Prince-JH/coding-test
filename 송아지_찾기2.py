if __name__ == '__main__':
    n = 13
    target = 35
    cnt = [0] * 10000
    ch = [0] * 10000
    ch[5] = 1
    queue = list()
    queue.append(5)

    while queue:
        temp = queue.pop(0)
        if temp == target:
            break
        for i in (temp - 1, temp + 1, temp + 5):
            if 0 <= i <= 10000:
                if ch[i] == 0:
                    queue.append(i)
                    cnt[i] = cnt[temp] + 1
                    ch[i] = 1

    print(cnt[target])

