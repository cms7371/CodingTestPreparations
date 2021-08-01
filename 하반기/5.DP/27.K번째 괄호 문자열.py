# https://www.acmicpc.net/problem/1023
N, K = map(int, input().split())
dp = [[0] * 51 for _ in range(N)]
dp[0][1] = 1

for pos in range(1, N):
    for open_p in range(0, 51):
        if pos > 0:
            if open_p < 50:
                dp[pos][open_p] += dp[pos - 1][open_p + 1]  # 괄호를 닫는 경우
                if open_p > 0:
                    dp[pos][open_p] += dp[pos - 1][open_p - 1]  # 괄호를 여는 경우
if dp[N - 1][0] < K + 1:
    result = -1
else:
    k = K + 1
    pos, open_p = N - 1, 0
    result = ''
    while pos > 0:
        if open_p < 51 and dp[pos - 1][open_p + 1] >= k:  # 현재에서 괄호를 여는 경우 '('
            open_p += 1
            result += '('
        else:
            k -= dp[pos - 1][open_p + 1]
            open_p -= 1
            result += ')'
        pos -= 1
    result += ')'
print(result)