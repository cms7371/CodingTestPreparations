# https://www.acmicpc.net/problem/1956
from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(node):
    result = INF
    pq = [(0, node)]
    dist = [INF] * (V + 1)
    dist[node] = 0
    while pq:
        d, cur = heappop(pq)
        if d <= dist[cur]:
            for _next, dd in path[cur]:
                if _next == node:
                    result = min(result, d + dd)
                elif d + dd < dist[_next]:
                    dist[_next] = d + dd
                    heappush(pq, (d + dd, _next))
    return result


V, E = map(int, input().split())
path = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    path[s].append((e, d))
answer = INF
for i in range(1, V + 1):
    answer = min(answer, dijkstra(i))
print(-1 if answer == INF else answer)