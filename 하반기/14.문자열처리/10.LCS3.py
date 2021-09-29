# https://www.acmicpc.net/problem/1958
s1, s2, s3 = input(), input(), input()
L, M, N = len(s1), len(s2), len(s3)
dp = [[[0] * (N + 1) for _ in range(M + 1)] for _ in range(L + 1)]
for i in range(L):
    for j in range(M):
        for k in range(N):
            dp[i + 1][j + 1][k + 1] = max(dp[i][j][k + 1], dp[i][j + 1][k],
                                          dp[i + 1][j][k], dp[i][j + 1][k + 1],
                                          dp[i + 1][j][k + 1], dp[i + 1][j + 1][k])
            if s1[i] == s2[j] and s2[j] == s3[k]:
                dp[i + 1][j + 1][k + 1] = max(dp[i + 1][j + 1][k + 1], dp[i][j][k] + 1)
print(dp[-1][-1][-1])
