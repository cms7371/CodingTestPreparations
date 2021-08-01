# https://www.acmicpc.net/problem/12865
n, k = map(int, input().split())
stuffs = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = stuffs[i - 1]
        if j >= w:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[-1][-1])