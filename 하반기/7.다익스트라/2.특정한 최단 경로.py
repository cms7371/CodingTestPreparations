# https://www.acmicpc.net/problem/1504

from heapq import heappush, heappop
import sys


def dijkstra(node):
    arr = [10e9] * (V + 1)
    pq = [(0, node)]
    while pq:
        d, current = heappop(pq)
        if d >= arr[current]:
            continue
        arr[current] = d
        for _next, w in path[current]:
            heappush(pq, (d + w, _next))
    return arr


input = sys.stdin.readline
V, E = map(int, input().split())
path = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    path[s].append((e, d))
    path[e].append((s, d))
via_1, via_2 = map(int, input().split())
dist_start = dijkstra(1)
dist_via1 = dijkstra(via_1)
dist_via2 = dijkstra(via_2)
result = min(dist_start[via_1] + dist_via1[via_2] + dist_via2[V], dist_start[via_2] + dist_via2[via_1] + dist_via1[V])
result = result if result < 10e9 else -1
print(result)
