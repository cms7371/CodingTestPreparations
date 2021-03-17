# 1012번 유기농 배추 https://www.acmicpc.net/problem/1012
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
t = int(input())
output = []
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[False] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = True
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                result += 1
                q = deque()
                q.append((i, j))
                graph[i][j] = False
                while q:
                    x, y = q.popleft()
                    for o in offsets:
                        nx, ny = x + o[0], y + o[1]
                        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                            graph[nx][ny] = False
                            q.append((nx, ny))
    output.append(str(result))
print("\n".join(output))





