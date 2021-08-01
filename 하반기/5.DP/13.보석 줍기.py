# https://www.acmicpc.net/problem/2208
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
pSum = [nums[0]]
for i in range(1, n):
    pSum.append(pSum[-1] + nums[i])
dp = [0] * n
dp[m - 1] = pSum[m - 1]
result = 0
for i in range(m, n):
    dp[i] = max(dp[i - 1] + nums[i], pSum[i] - pSum[i - m])
    result = max(dp[i], result)
print(result)

