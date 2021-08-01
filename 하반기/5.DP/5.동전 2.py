# https://www.acmicpc.net/problem/2294
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [10e9] * (k + 1)
dp[0] = 0
for i in range(k + 1):
    if dp[i] != 10e9:
        for c in coins:
            if i + c <= k:
                dp[i + c] = min(dp[i + c], dp[i] + 1)
print(-1 if dp[-1] == 10e9 else dp[-1])