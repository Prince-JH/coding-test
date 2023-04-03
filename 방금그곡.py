def change(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'D#' in music:
        music = music.replace('D#', 'd')
    return music


def solution(m, musicinfos):
    notes = change(m)
    answer = []

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
        title = info[2]

        sequence = ''

        converted_melody = change(melody)

        for i in range(duration):
            sequence += converted_melody[i % len(converted_melody)]

        if notes in sequence:
            answer.append([len(answer), duration, title])

    if not answer:
        return "(None)"
    return sorted(answer, key=lambda x: (-x[1], x[0]))[0][2]
