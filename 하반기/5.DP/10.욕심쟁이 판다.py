# https://www.acmicpc.net/problem/1937
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
positions = []
for i in range(n):
    for j in range(n):
        positions.append((table[i][j], i, j))
positions.sort()
while positions:
    val, y, x = positions.pop()
    for dy, dx in offsets:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and table[ny][nx] < val:
            dp[ny][nx] = max(dp[ny][nx], dp[y][x] + 1)
print(max([max(line) for line in dp]))


