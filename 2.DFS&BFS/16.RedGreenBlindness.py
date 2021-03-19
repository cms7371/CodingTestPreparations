# 10026번 적록색약
import sys
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def dfs(g, x, y, chars):
    for o in offsets:
        nx, ny = x + o[0], y + o[1]
        if 0 <= nx < n and 0 <= ny < n and g[nx][ny] is not None and g[nx][ny] in chars:
            g[nx][ny] = None
            dfs(g, nx, ny, chars)
n = int(input())
sys.setrecursionlimit(n * n)
origin = [list(input()) for _ in range(n)]
normal = [[i for i in line] for line in origin]
abnormal = [[i for i in line] for line in origin]
result1 = 0
result2 = 0
for i in range(n):
    for j in range(n):
        if normal[i][j] is not None:
            result1 += 1
            c = normal[i][j]
            normal[i][j] = None
            dfs(normal, i, j, c)
for i in range(n):
    for j in range(n):
        if abnormal[i][j] is not None:
            result2 += 1
            c = abnormal[i][j]
            abnormal[i][j] = None
            dfs(abnormal, i, j, "RG" if c == "R" or c == "G" else "B")
print(result1, result2)
