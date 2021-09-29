# https://programmers.co.kr/learn/courses/30/lessons/17677
from collections import defaultdict


def solution(str1, str2):
    pool1 = []
    for i in range(len(str1) - 1):
        sub = str1[i: i + 2].lower()
        if sub.isalpha():
            pool1.append(sub)
    pool2 = []
    for i in range(len(str2) - 1):
        sub = str2[i: i + 2].lower()
        if sub.isalpha():
            pool2.append(sub)
    counter1 = defaultdict(int)
    set1 = set()
    for sub in pool1:
        counter1[sub] += 1
        set1.add(sub + str(counter1[sub]))
    counter2 = defaultdict(int)
    set2 = set()
    for sub in pool2:
        counter2[sub] += 1
        set2.add(sub + str(counter2[sub]))
    if len(set1) == 0 and len(set2) == 0:
        return 65536
    answer = int(len(set1.intersection(set2)) / len(set1.union(set2)) * 65536)
    return answer
