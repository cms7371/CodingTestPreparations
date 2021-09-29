# https://programmers.co.kr/learn/courses/30/lessons/12978
from heapq import *
INF = 10 ** 9




def solution(N, road, K):
    answer = 0
    dist = [INF] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for s, e, d in road:
        graph[s].append((e, d))
        graph[e].append((s, d))
    q = [(0, 1)]
    dist[1] = 0
    while q:
        d, cur = heappop(q)
        if d <= dist[cur]:
            for nxt, dd in graph[cur]:
                if d + dd <= K and d + dd < dist[nxt]:
                    dist[nxt] = d + dd
                    heappush(q, (d + dd, nxt))
    answer = sum(d <= K for d in dist)
    return answer