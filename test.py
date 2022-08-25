def solution(S):
    if 'a' not in S or 'b' not in S:
        return True
    else:
        temp = sorted(S)
        a_cnt = temp.index('b')
        print(a_cnt)
        for i in range(a_cnt):
            if S[i] == 'b':
                return False
        return True


if __name__ == '__main__':
    d1 = {"name": "Alex", "age": 25}
    d2 = {"name": "Alex", "city": "New York"}

    print(**d1)
    merged_dict = {**d1, **d2}
    print(merged_dict)
