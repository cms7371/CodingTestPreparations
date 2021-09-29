# https://www.acmicpc.net/problem/9370
from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    path = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g):
            d -= 0.5
        path[a].append((b, d))
        path[b].append((a, d))
    candidate = [int(input()) for _ in range(t)]
    candidate.sort()
    dist = [INF] * (n + 1)
    possible_node = [False] * (n + 1)
    dist[s] = 0
    pq = [(0, s, False)]
    while pq:
        d, cur, is_possible = heappop(pq)
        if d <= dist[cur]:
            if is_possible:
                possible_node[cur] = True
            for _next, dd in path[cur]:
                if d + dd < dist[_next]:
                    dist[_next] = d + dd
                    heappush(pq, (d + dd, _next,
                                  True if (cur == g and _next == h) or (cur == h and _next == g) else is_possible))
    candidate = [c for c in candidate if possible_node[c]]
    print(*candidate)
