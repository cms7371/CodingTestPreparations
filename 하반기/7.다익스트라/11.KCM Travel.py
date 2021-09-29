# https://www.acmicpc.net/problem/10217
# DP를 이용한 풀이
import sys
input = sys.stdin.readline
INF = 10 ** 9
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(K):
        s, e, c, d = map(int, input().split())
        graph[s].append((e, c, d))
    dp = [[INF] * (N + 1) for _ in range(M + 1)]
    dp[0][1] = 0
    for c in range(M + 1):
        for n in range(1, N + 1):
            if dp[c][n] == INF:
                continue
            d = dp[c][n]
            for nn, nc, nd in graph[n]:
                if c + nc <= M and d + nd < dp[c + nc][nn]:
                    dp[c + nc][nn] = d + nd
    result = min([dp[m][N] for m in range(M + 1)])
    print('Poor KCM' if result == INF else result)


# 다익스트라를 활용한 풀이 파이썬에서는 시간초과가 남
from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(K):
        s, e, c, d = map(int, input().split())
        graph[s].append((e, c, d))
    dist = [[INF] * (N + 1) for _ in range(M + 1)]
    dist[0][1] = 0
    q = [(0, 1, 0)]  # d, node, c 순서
    while q:
        d, cur, c = heappop(q)
        if d <= dist[c][cur]:
            for _next, cc, dd in graph[cur]:
                if c + cc <= M and d + dd < dist[c + cc][_next]:
                    dist[c + cc][_next] = d + dd
                    heappush(q, (d + dd, _next, c + cc))
    result = min([dist[m][N] for m in range(M + 1)])
    print('Poor KCM' if result == INF else result)