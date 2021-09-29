# https://www.acmicpc.net/problem/2098
from collections import deque

INF = 10 ** 9
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[INF] * (2 ** N) for _ in range(N)]
q = deque()
q.append((0, 0, 1))
result = INF
while q:
    cur, d, mask = q.popleft()
    if d > dp[cur][mask]:
        continue
    if mask == (2 ** N - 1) and graph[cur][0]:
        result = min(d + graph[cur][0], result)
        continue
    for i in range(1, N):
        if graph[cur][i] and not (mask & (2 ** i)):
            n_mask = mask | (2 ** i)
            dd = d + graph[cur][i]
            if dd < dp[i][n_mask]:
                dp[i][n_mask] = dd
                q.append((i, dd, n_mask))
print(result)