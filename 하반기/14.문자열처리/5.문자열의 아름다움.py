# https://programmers.co.kr/learn/courses/30/lessons/68938

from itertools import groupby

def solution(s):
    answer = 0
    n = len(s)
    for i in range(n - 1):
        idx_of_dif = -1
        local_max = 0
        for j in range(i + 1, n):
            if s[i] != s[j]:
                answer += j - i
                local_max = j - i
                if idx_of_dif == -1:
                    idx_of_dif = j
            else:
                if idx_of_dif != -1:
                    local_max = max(local_max, j - idx_of_dif)
                answer += local_max
    return answer