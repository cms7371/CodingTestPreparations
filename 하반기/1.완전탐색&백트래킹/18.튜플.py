# https://programmers.co.kr/learn/courses/30/lessons/64065
# 2019 카카오 인턴십
from collections import defaultdict


def solution(s):
    split_s = s[2:-2].split('},{')
    tuple_set = [list(map(int, line.split(','))) for line in split_s]
    tuple_set.sort(key=len)
    answer = []
    c_dict = defaultdict(int)
    for component in tuple_set:
        n_dict = defaultdict(int)
        for c in component:
            n_dict[c] += 1
            if n_dict[c] > c_dict[c]:
                c_dict[c] += 1
                answer.append(c)
                break
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))