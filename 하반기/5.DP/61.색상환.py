# https://www.acmicpc.net/problem/2482
MOD = 1000000003
N = int(input())
K = int(input())
# dp[i][k] i번째 k개가 됐을 때 경우의 수인데 f가 0이면 첫번째를 안 뽑은 것, 아니면 뽑은 것
dp = [[0] * (K + 1) for _ in range(N)]
for i in range(N):
    dp[i][0] = 1
    dp[i][1] = i + 1
for i in range(2, N):
    for k in range(2, K + 1):
        dp[i][k] = dp[i - 1][k] + dp[i - 2][k - 1]
        if i == N - 1:
            dp[i][k] = dp[i - 1][k] + dp[i - 3][k - 1]
print(dp[-1][-1] % MOD)
print(*dp, sep='\n')