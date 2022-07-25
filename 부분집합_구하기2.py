def DFS(L, num, temp):
    if L == num:
        for i in range(len(temp)):
            if temp[i] == 1:
                print(i + 1, end=' ')
        print()
    else:
        temp[L] = 1
        DFS(L + 1, num, temp)
        temp[L] = 0
        DFS(L + 1, num, temp)

if __name__ == '__main__':
    num = 3
    temp = [0] * num
    DFS(0, num, temp)