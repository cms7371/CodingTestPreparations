# https://www.acmicpc.net/problem/2211
from heapq import *
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
dist = [10 ** 9] * (N + 1)
q = [(0, 1, 1)]
result = []
while q:
    d, cur, prev = heappop(q)
    if d < dist[cur]:
        dist[cur] = d
        result.append((prev, cur))
        for _next, dd in graph[cur]:
            if d + dd < dist[_next]:
                heappush(q, (d + dd, _next, cur))
print(len(result) - 1)
for s, e in result[1:]:
    print(s, e)