# https://www.acmicpc.net/problem/5582
s1 = input()
s2 = input()
dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
print(max(max(line) for line in dp))