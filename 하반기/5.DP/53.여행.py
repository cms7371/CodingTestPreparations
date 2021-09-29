# https://www.acmicpc.net/problem/2157
import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
path = [[] for _ in range(N + 1)]
for _ in range(K):
    s, e, c = map(int, input().split())
    if s >= e:
        continue
    path[s].append((e, c))
dp = [[-1] * M for _ in range(N + 1)]
dp[1][0] = 0
for s in range(1, N + 1):
    for m in range(0, M - 1):
        if dp[s][m] != -1:
            for e, c in path[s]:
                dp[e][m + 1] = max(dp[e][m + 1], dp[s][m] + c)
print(max(dp[-1]))