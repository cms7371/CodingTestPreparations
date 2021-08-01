# https://www.acmicpc.net/problem/16118  -> 파이썬은 통과 못할 코드.... 이해했으니 넘어가는걸로

from heapq import heappush, heappop
import sys


input = sys.stdin.readline
INF = int(10e9)
N, M = map(int, input().split())
path = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    path[s].append((e, d * 2))
    path[e].append((s, d * 2))
# 여우의 거리를 구하는 부분
dist_fox = [INF] * (N + 1)
pq = [(0, 1)]
while pq:
    d, now = heappop(pq)
    if d < dist_fox[now]:
        dist_fox[now] = d
        for _next, nd in path[now]:
            heappush(pq, (nd + d, _next))
dist_wolf = [[INF, INF] for _ in range(N + 1)]
pq = [(0, 1, 1)]

while pq:
    d, now, boost = heappop(pq)
    if d < dist_wolf[now][boost]:
        dist_wolf[now][boost] = d
        for _next, nd in path[now]:
            if boost:
                heappush(pq, (d + (nd // 2), _next, 0))
            else:
                heappush(pq, (d + (nd * 2), _next, 1))
result = 0
for i in range(2, N + 1):
    if dist_fox[i] < min(dist_wolf[i]):
        result += 1
print(result)