# 14500번 테트로미노
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(n):
    for j in range(m):
        stack = [(i, j, graph[i][j], -1, 1)]
        while stack:
            x, y, val, d, jump = stack.pop()
            if jump == 4:
                result = max(result, val)
                continue
            for k in range(4):
                if (k + 2) % 4 != d:
                    nx, ny = x + offsets[k][0], y + offsets[k][1]
                    if 0 <= nx < n and 0 <= ny < m:
                        nval = val + graph[nx][ny]
                        stack.append((nx, ny, nval, k, jump + 1))
        around_val = [0, 0, 0, 0]
        for k in range(4):
            nx, ny = i + offsets[k][0], j + offsets[k][1]
            if 0 <= nx < n and 0 <= ny < m:
                around_val[k] = graph[nx][ny]
        cross_sum = sum(around_val) + graph[i][j]
        for val in around_val:
            result = max(result, cross_sum - val)
print(result)


