# https://www.acmicpc.net/problem/2293
# 첫 풀이 -> 메모리초과. 굳이 dp테이블이 2차원일 필요가 잇을까?
# n, k = map(int, input().split())
# coins = [int(input()) for _ in range(n)]
# dp = [[0] * (k + 1) for _ in range(n + 1)]  # n번째 코인까지 이용했을 때 k를 만들 수 있는 경우의 수에 대한 dp
# for i in range(n + 1):
#     dp[i][0] = 1
# for i in range(1, n + 1):
#     for j in range(1, k + 1):
#         dp[i][j] = dp[i - 1][j]
#         if j >= coins[i - 1]:
#             dp[i][j] += dp[i][j - coins[i - 1]]
# print(dp[-1][-1])
# 두 번째 풀이
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)  # n번째 코인까지 이용했을 때 k를 만들 수 있는 경우의 수에 대한 dp
dp[0] = 1
for c in coins:
    for j in range(1, k + 1):
        if j >= c:
            dp[j] += dp[j - c]
print(dp[-1])