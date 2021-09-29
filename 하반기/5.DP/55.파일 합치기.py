# https://www.acmicpc.net/problem/11066
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    p_sum = arr[:]
    p_sum.append(0)
    for idx in range(1, N):
        p_sum[idx] += p_sum[idx - 1]
    dp = [[0] * N for _ in range(N)]
    for l in range(1, N):
        for i in range(N - l):
            dp[i][i + l] = min(dp[i][k] + dp[k + 1][i + l] + p_sum[i + l] - p_sum[i - 1] for k in range(i, i + l))
    print(dp[0][N - 1])