# https://www.acmicpc.net/problem/1800
from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 7


N, P, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(P):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
left, right = 0, 1000000
while left <= right:
    mid = (left + right + 1) // 2
    pq = [(0, 1)]
    visited = [INF] * (N + 1)
    visited[1] = 0
    while pq:
        skip, node = heappop(pq)
        if skip <= visited[node]:
            for nxt, weight in graph[node]:
                if skip < K and weight > mid and visited[nxt] > skip + 1:
                    visited[nxt] = skip + 1
                    heappush(pq, (skip + 1, nxt))
                elif weight <= mid and visited[nxt] > skip:
                    visited[nxt] = skip
                    heappush(pq, (skip, nxt))
    if visited[N] != INF:
        right = mid - 1
    else:
        left = mid + 1
print(-1 if left > 1000000 else left)



    # 가능 -> right = mid - 1
    # 불가능 -> left = mid + 1