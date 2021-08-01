# https://www.acmicpc.net/problem/2169
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
dp = table[0][:]
for i in range(1, m):
    dp[i] += dp[i - 1]
for i in range(1, n):
    for j in range(m):
        dp[j] += table[i][j]
    dp_left = dp[:]
    for j in range(m - 1):
        dp_left[j + 1] = max(dp[j + 1], dp_left[j] + table[i][j + 1])
    dp_right = dp[:]
    for j in range(m - 1, 0, -1):
        dp_right[j - 1] = max(dp[j - 1], dp_right[j] + table[i][j - 1])
    dp = [max(dp_right[j], dp_left[j]) for j in range(m)]
print(dp[-1])


