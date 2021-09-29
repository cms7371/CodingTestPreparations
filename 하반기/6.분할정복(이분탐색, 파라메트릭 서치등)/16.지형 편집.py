# https://programmers.co.kr/learn/courses/30/lessons/12984
from collections import Counter


def solution(land, P, Q):
    h_val = [val for line in land for val in line]
    counter = Counter(h_val)
    h_val = list(counter.keys())
    h_val.sort()
    cost = sum(key * val for key, val in counter.items()) * Q
    print(cost)
    lower_sum, last_h = 0, 0
    n = len(land)
    total = n * n
    for h in h_val:
        diff = (P * lower_sum - (total - lower_sum) * Q) * (h - last_h)
        lower_sum += counter[h]
        last_h = h
        if diff > 0:
            break
        cost += diff
        print(diff, cost)
    return cost


print(solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3))
