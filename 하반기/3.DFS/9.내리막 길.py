# https://www.acmicpc.net/problem/1520
# dp + DFS
import sys
sys.setrecursionlimit(10 ** 9)


def DFS(y, x):
    if dp[y][x] == -1:
        dp[y][x] = 0
        global N, M
        for dy, dx in offsets:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] < graph[y][x]:
                dp[y][x] += DFS(ny, nx)
    return dp[y][x]


offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
dp[-1][-1] = 1
print(DFS(0, 0))





