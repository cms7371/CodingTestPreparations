# https://www.acmicpc.net/problem/1753
from heapq import heappush, heappop
import sys


input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
path = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    path[s].append((e, d))
dist = [10e9] * (V + 1)
pq = [(0, start)]
while pq:
    d, current = heappop(pq)
    if d >= dist[current]:
        continue
    dist[current] = d
    for _next, w in path[current]:
        heappush(pq, (d + w, _next))
for i in range(1, V + 1):
    print(dist[i] if dist[i] != 10e9 else 'INF')
