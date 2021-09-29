# https://programmers.co.kr/learn/courses/30/lessons/17683
import re


def conv_s(s):
    if len(s) == 2:
        return s[0].lower()
    return s


def solution(m, musicinfos):
    answer = ''
    answer_d = 0
    sep_m = re.findall("[A-Z]#?", m)
    m = "".join(conv_s(s) for s in sep_m)
    for info in musicinfos:
        start, end, name, partial_sound = info.split(',')
        duration = time_to_min(end) - time_to_min(start)
        duration += 24 * 60 if duration < 0 else 0
        total_sound = recovered_sound(partial_sound, duration)
        if duration > answer_d and total_sound.find(m) >= 0:
            answer = name
            answer_d = duration
    if answer == "":
        return "(None)"
    return answer


def time_to_min(time):
    hh, mm = map(int, time.split(":"))
    return hh * 60 + mm


def recovered_sound(sound, duration):
    sep_sound = re.findall("[A-Z]#?", sound)
    result = [conv_s(sep_sound[i % len(sep_sound)]) for i in range(duration)]
    return "".join(result)