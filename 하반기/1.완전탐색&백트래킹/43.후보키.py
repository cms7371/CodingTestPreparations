# https://programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations


def solution(relation):
    set_result = []
    r, c = len(relation), len(relation[0])
    for i in range(1, c + 1):
        comb = combinations(range(c), i)
        for cols in comb:
            if len(set(map(lambda row: get_joined_s(row, cols), relation))) == r and all(
                    map(lambda x: not_subset(x, set(cols)), set_result)):
                set_result.append(set(cols))
    return len(set_result)


def get_joined_s(row, cols):
    result = ""
    for c in cols:
        result += row[c]
    return result


def not_subset(small_s, big_s):
    if big_s.intersection(small_s) == small_s:
        return False
    return True


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
