# https://www.acmicpc.net/problem/2225
MOD = 10 ** 9


N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0] = [1] * (K + 1)
for k in range(1, K + 1):
    for n in range(1, N + 1):
        for o in range(0, n + 1):
            dp[n][k] += dp[n - o][k - 1]
        dp[n][k] %= MOD
print(dp[N][K])
print(*dp, sep='\n')