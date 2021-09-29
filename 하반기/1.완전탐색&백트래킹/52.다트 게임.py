# https://programmers.co.kr/learn/courses/30/lessons/17682
import re


def solution(dartResult):
    sep_result = re.findall("\\d+[^\\d]+", dartResult)
    result = []
    for cur_s in sep_result:
        if cur_s[1].isdigit():
            num = int(cur_s[:2])
            remaining = cur_s[2:]
        else:
            num = int(cur_s[:1])
            remaining = cur_s[1:]
        if remaining[0] == 'D':
            num **= 2
        elif remaining[0] == 'T':
            num **= 3
        if len(remaining) == 2:
            if remaining[-1] == '*':
                num *= 2
                if result:
                    result[-1] *= 2
            elif remaining[-1] == '#':
                num *= -1
        result.append(num)
    print(result)
    return sum(result)