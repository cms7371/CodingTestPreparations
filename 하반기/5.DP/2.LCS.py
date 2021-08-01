# https://www.acmicpc.net/problem/9251
# 자세한 이론 https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence
str1 = input()
str2 = input()
n1 = len(str1)
n2 = len(str2)
dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
# LCS의 길이를 구하는 부분
for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
# dp 테이블을 이용하여 LCS를 직접 찾기
idx1 = n1
idx2 = n2
result = []
while dp[idx1][idx2] != 0:
    if dp[idx1][idx2] == dp[idx1][idx2 - 1]:
        idx2 -= 1
    elif dp[idx1][idx2] == dp[idx1 - 1][idx2]:
        idx1 -= 1
    else:
        result.append(str1[idx1 - 1])
        idx1 -= 1
        idx2 -= 1
print(*result[::-1], sep="")
