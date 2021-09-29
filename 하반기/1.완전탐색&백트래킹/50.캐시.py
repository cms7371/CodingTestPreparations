# https://programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque


def solution(cacheSize, cities):
    time = 0
    cache = deque()
    for c in cities:
        c = c.lower()
        if c in cache:
            time += 1
            cache.remove(c)
            cache.append(c)
        else:
            cache.append(c)
            if len(cache) > cacheSize:
                cache.popleft()
            time += 5
    return time

