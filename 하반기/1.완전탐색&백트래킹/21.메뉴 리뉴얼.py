# https://programmers.co.kr/learn/courses/30/lessons/72411
# 2021 KAKAO BLIND RECUITMENT
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    for c in course:
        counter = defaultdict(int)
        for o in orders:
            if len(o) >= c:
                for comb in combinations(sorted(o), c):
                    counter["".join(comb)] += 1
        if counter:
            c_max = max(counter.values())
            if c_max > 1:
                answer.extend([comb for comb in counter if counter[comb] == c_max])
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))