# https://www.acmicpc.net/problem/17404
import sys
input = sys.stdin.readline
INF = 10 ** 9
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
# dp[f][i][c] 첫번째를 f로 색칠, i 번째 집을 c로 할 때 최소 비용
dp = [[[INF] * 3 for _ in range(N)] for _ in range(3)]
for i in range(3):
    dp[i][0][i] = cost[0][i]
for f in range(3):
    for i in range(1, N):
        for c in range(3):
            if i == N - 1 and f == c:
                continue
            dp[f][i][c] = cost[i][c] + min(dp[f][i - 1][pc] for pc in range(3) if pc != c)
print(min(min(dp[f][-1]) for f in range(3)))