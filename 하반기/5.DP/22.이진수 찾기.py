# https://www.acmicpc.net/problem/2248
# 발상이 상당히 어려운 문제
N, L, I = map(int, input().split())
# 처음에는 n자리 수를 가지며 l개 이하의 1을 가지는 이진수의 개수를 나타내는 dp[n][l]을 구함
dp = [[0] * (L + 1) for _ in range(N + 1)]
dp[1][0], dp[0][0] = 1, 1
for i in range(1, L + 1):
    dp[1][i] = 2
    dp[0][i] = 1
for i in range(2, N + 1):
    for j in range(L + 1):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
l = L
i = I
result = ""
for n in range(N, 0, -1):
    if dp[n - 1][l] < i:
        result += '1'
        i -= dp[n - 1][l]
        l -= 1
    else:
        result += '0'
print(result)