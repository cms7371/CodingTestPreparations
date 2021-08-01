# 2583번 영역 구하기 https://www.acmicpc.net/problem/2583
from collections import deque

offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m, k = map(int, input().split())

graph = [[False] * m for _ in range(n)]
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = True
result = []
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            count = 1
            graph[i][j] = True
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.pop()
                for o in offsets:
                    nx, ny = x + o[0], y + o[1]
                    if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:
                        graph[nx][ny] = True
                        q.append((nx, ny))
                        count += 1
            result.append(count)
result.sort()
print(len(result))
print(" ".join(map(str, result)))
