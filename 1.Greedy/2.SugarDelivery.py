# 2839번 : 설탕 배달 https://www.acmicpc.net/problem/2839
# dp 테이블을 이용한 다이나믹 프로그래밍 문제

INF = int(1e9)
n = int(input())
dp = [INF] * (n + 1)
dp[3] = 1
if n > 4:
    dp[5] = 1
    for i in range(6, n + 1):
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
if dp[n] < INF:
    print(dp[n])
else:
    print(-1)

# 사워하다 생각난 다른 방법 -> 5킬로를 최대한 많이 하는 것으로 시작해서 부족하면 + 3 많으면 -5 + 3을 하여 적정 값을 찾아냄




