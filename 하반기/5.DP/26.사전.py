# https://www.acmicpc.net/problem/1256
N, M, K = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(0, N + 1):
    dp[0][i] = 1
for j in range(1, M + 1):
    dp[j][0] = 1
for z in range(1, M + 1):
    for a in range(1, N + 1):
        dp[z][a] = dp[z - 1][a] + dp[z][a - 1]
if dp[M][N] < K:
    result = '-1'
else:
    n, m, k = N, M, K
    result = ''
    while n != 0 or m != 0:
        if n > 0 and dp[m][n - 1] >= k:
            result += 'a'
            n -= 1
        else:
            result += 'z'
            k -= dp[m][n - 1] if n > 0 else 0
            m -= 1
print(result)
