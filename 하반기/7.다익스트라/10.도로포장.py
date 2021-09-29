# https://www.acmicpc.net/problem/1162
from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 12
N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
dist = [[INF] * (N + 1) for _ in range(K + 1)]
dist[1][0] = 0
q = [(0, 1, 0)]
while q:
    d, cur, k = heappop(q)
    if d <= dist[k][cur]:
        for _next, dd in graph[cur]:
            if d + dd < dist[k][_next]:
                dist[k][_next] = d + dd
                q.append((d + dd, _next, k))
            if k < K and d < dist[k + 1][_next]:
                dist[k + 1][_next] = d
                q.append((d, _next, k + 1))
print(min([dist[k][N] for k in range(K + 1)]))



