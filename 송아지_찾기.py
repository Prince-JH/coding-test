if __name__ == '__main__':
    n = 5
    target = 14
    check = [0] * 10000
    dis = [0] * 10000
    check[n] = 1
    dis[n] = 0
    queue = list()
    queue.append(n)
    while queue:
        now = queue.pop(0)
        if now == target:
            break
        for next in (now - 1, now + 1, now + 5):
            if 0 < next <= 10000:
                if check[next] == 0:
                    queue.append(next)
                    check[next] = 1
                    dis[next] = dis[now] + 1
    print(dis[target])


