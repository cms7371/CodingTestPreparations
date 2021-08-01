# 2638번 치즈 https://www.acmicpc.net/problem/2638
from collections import deque
import sys
input = sys.stdin.readline
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cheese_num = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cheese_num += 1
time = 0
while cheese_num > 0:
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque()
    q.append((0, 0))
    out_cheese = []
    while q:
        x, y = q.popleft()
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                else:
                    out_cheese.append((nx, ny))
    melt_cheese = []
    for x, y in out_cheese:
        count = 0
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if graph[nx][ny] == 0 and visited[nx][ny]:
                count += 1
        if count > 1:
            melt_cheese.append((x, y))
    for x, y in melt_cheese:
        cheese_num -= 1
        graph[x][y] = 0
    time += 1
print(time)



