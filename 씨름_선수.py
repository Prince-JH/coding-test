if __name__ == '__main__':
    players = [(172, 67), (183, 65), (180, 70), (170, 72), (181, 60)]
    players.sort(reverse=True)
    print(players)
    cnt = 0

    last = None

    for player in players:
        if last:
            if player[0] > last[0] or player[1] > last[1]:
                cnt += 1
                last = player
        else:
            cnt += 1
            last = player

    print(cnt)
