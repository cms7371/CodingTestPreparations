# https://www.acmicpc.net/problem/1463
n = int(input())
dp = [10e9] * (n + 1)
dp[1] = 0
for i in range(1, n):
    if i * 2 <= n:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    if i * 3 <= n:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    dp[i + 1] = min(dp[i + 1], dp[i] + 1)
print(dp[n])