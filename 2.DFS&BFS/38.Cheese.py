# 2636번 치즈 https://www.acmicpc.net/problem/2636
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
time = 0
last_cheese = 0
while True:
    q = deque()
    melt_list = []
    visited = [[False] * m for _ in range(n)]
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 1:
                    melt_list.append((nx, ny))
                else:
                    q.append((nx, ny))
    if len(melt_list) == 0:
        break
    time += 1
    last_cheese = len(melt_list)
    for x, y in melt_list:
        graph[x][y] = 0
print(time, last_cheese, sep="\n")



