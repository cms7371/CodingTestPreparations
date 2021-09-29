# https://www.acmicpc.net/problem/15422
from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 12
N, M, F, S, E = map(int, input().split())
road = [[] for _ in range(N)]
flight = [[] for _ in range(N)]
for _ in range(M):
    s, e, w = map(int, input().split())
    road[s].append((e, w))
    road[e].append((s, w))
for _ in range(F):
    s, e = map(int, input().split())
    flight[s].append(e)
dist = [INF] * N
dist_f = [INF] * N
dist[S], dist_f[S] = 0, 0
q = [(0, S, True)]
while q:
    cost, cur, CanFly = heappop(q)
    if CanFly and cost <= dist[cur]:
        for node, d in road[cur]:
            if cost + d < dist[node]:
                dist[node] = cost + d
                heappush(q, (cost + d, node, True))
        for node in flight[cur]:
            if cost < dist_f[node]:
                dist_f[node] = cost
                heappush(q, (cost, node, False))
    elif not CanFly and cost <= dist_f[cur]:
        for node, d in road[cur]:
            if cost + d < dist_f[node]:
                dist_f[node] = cost + d
                heappush(q, (cost + d, node, False))
print(min(dist[E], dist_f[E]))
