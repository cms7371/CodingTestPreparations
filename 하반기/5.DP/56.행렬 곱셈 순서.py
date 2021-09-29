# https://www.acmicpc.net/problem/11049


N = int(input())
dp = [[None] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = [*map(int, input().split()), 0]
for l in range(1, N):
    for i in range(N - l):
        dp[i][i + l] = [0, 0, 2 ** 31]
        for k in range(i, i + l):
            cur_val = dp[i][k][0] * dp[i][k][1] * dp[k + 1][i + l][1] + dp[i][k][2] + dp[k + 1][i + l][2]
            if dp[i][i + l][2] > cur_val:
                dp[i][i + l] = [dp[i][k][0], dp[k + 1][i + l][1], cur_val]
print(dp[0][N - 1][2])
print(*dp, sep='\n')