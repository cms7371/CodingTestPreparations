# https://www.acmicpc.net/problem/10942
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [[False] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = True
    if i < N - 1 and arr[i] == arr[i + 1]:
        dp[i][i + 1] = True
for l in range(2, N):
    for i in range(N - l):
        if dp[i + 1][i + l - 1] and arr[i] == arr[i + l]:
            dp[i][i + l] = True
Q = int(input())
for _ in range(Q):
    q1, q2 = map(int, input().split())
    print(int(dp[q1 - 1][q2 - 1]))

