# https://www.acmicpc.net/problem/9465
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][1], dp[1][1] = sticker[0][0], sticker[1][0]
    for i in range(2, n + 1):
        for line in range(2):
            current = sticker[line][i - 1]
            dp[line][i] = max(dp[line][i - 2] + current, dp[line - 1][i - 1] + current, dp[line][i - 1])
    print(max(dp[0][-1], dp[1][-1]))



