# https://www.acmicpc.net/problem/1023
# 우선은 포기... 너무 어려움

N, K = map(int, input().split())
dp = [[[0, 0] for _ in range(101)] for _ in range(N)]  # 50을 기준으로 가중치 0 여는괄호')'가 오면 + 1 닫는괄호'('가 오면 -1
dp[0][49][1], dp[0][51][0] = 1, 1
for pos in range(1, N):
    for weight in range(0, 101):
        # w가 0 이상인 경우
        if weight >= 50:
            dp[pos][weight][0] += dp[pos - 1][weight - 1][0]  # 괄호를 여는 경우
            dp[pos][weight][1] += dp[pos - 1][weight - 1][1]
            if weight < 100:
                dp[pos][weight][0] += dp[pos - 1][weight + 1][0]  # 괄호를 닫는 경우
                dp[pos][weight][1] += dp[pos - 1][weight + 1][1]
        elif weight < 50:
            if weight > 0:
                dp[pos][weight][1] += dp[pos - 1][weight - 1][1]
            dp[pos][weight][1] += dp[pos - 1][weight + 1][0] + dp[pos - 1][weight + 1][1]
print(*dp, sep='\n')


