# https://www.acmicpc.net/problem/1562
MOD = 10 ** 9
N = int(input())
dp = [[[0] * 1024 for _ in range(10)] for _ in range(N + 1)]  # dp[n][d][m] n자리에 마지막이 d이고 m 마스크
for i in range(1, 10):
    dp[1][i][2 ** i] = 1
for n in range(1, N):
    for d in range(10):
        for m in range(1024):
            if dp[n][d][m]:
                dp[n][d][m] %= MOD
                if d != 9:
                    dp[n + 1][d + 1][m | (2 ** (d + 1))] += dp[n][d][m]
                if d != 0:
                    dp[n + 1][d - 1][m | (2 ** (d - 1))] += dp[n][d][m]
print(sum(dp[N][d][-1] for d in range(10)) % (10 ** 9) % MOD)
# print(*dp, sep='\n')