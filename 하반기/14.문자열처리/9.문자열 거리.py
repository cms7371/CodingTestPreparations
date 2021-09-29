# https://www.acmicpc.net/problem/1230

O = input()
N = input()
INF = 10 ** 9
dp = [[[INF, INF] for _ in range(len(N) + 1)] for _ in range(len(O) + 1)]
dp[0][0] = [0, INF]
for i in range(1, len(N) + 1):
    dp[0][i] = [INF, 1]
for i in range(len(O)):
    for j in range(len(N)):
        dp[i + 1][j + 1][0] = min(dp[i][j]) if O[i] == N[j] else INF
        dp[i + 1][j + 1][1] = min(dp[i + 1][j][0] + 1, dp[i + 1][j][1])
result = min(dp[-1][-1])
print(-1 if result >= INF else result)