# https://www.acmicpc.net/problem/1149
INF = int(10e9)
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF] * 3 for _ in range(n)]
dp[0] = cost[0]
for i in range(1, n):
    for c in range(3):
        for prev_c in range(3):
            if c != prev_c:
                dp[i][c] = min(dp[i][c], dp[i - 1][prev_c] + cost[i][c])
print(min(dp[-1]))