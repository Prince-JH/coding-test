def solution(name, yearning, photo):
    name_to_yearning = {name[i]: yearning[i] for i in range(len(name))}
    answer = []
    for _list in photo:
        score = 0
        for e in _list:
            score += name_to_yearning.get(e, 0)
        answer.append(score)
    return answer
