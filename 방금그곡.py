def solution(m, musicinfos):
    notes = ''
    idx = 0
    while idx < len(m):
        if idx + 1 < len(m) and m[idx + 1] == '#':
            notes += m[idx].lower()
            idx += 2
        else:
            notes += m[idx]
            idx += 1

    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        start = info[0].split(':')
        start_hour = int(start[0])
        start_min = int(start[1])
        end = info[1].split(':')
        end_hour = int(end[0])
        end_min = int(end[1])
        duration = (end_hour - start_hour) * 60 + (end_min - start_min)
        melody = info[3]
        sequence = ''

        idx = 0
        while idx < duration:
            if melody[(idx + 1) % len(melody)] == '#':
                sequence += melody[idx % len(melody)].lower()
                idx += 2
            else:
                sequence += melody[idx % len(melody)]
                idx += 1
        if notes in sequence:
            return info[2]
    return "(None)"

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
