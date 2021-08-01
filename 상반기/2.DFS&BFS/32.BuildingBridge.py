# 2146번 다리 만들기 https://www.acmicpc.net/problem/2146
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 섬을 구별하고 해안선을 찾음
island_num = 2
boundary = set()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = island_num
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for dx, dy in offsets:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] == 1:
                            graph[nx][ny] = island_num
                            q.append((nx, ny))
                        elif graph[nx][ny] == 0:
                            boundary.add((x, y))
            island_num += 1
result = 10e9
for i, j in boundary:
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((i, j, 0))
    num = graph[i][j]
    while q:
        x, y, d = q.popleft()
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    q.append((nx, ny, d + 1))
                    visited[nx][ny] = True
                elif graph[nx][ny] != num:
                    result = min(result, d)
                    q = False
                    break
print(result)






