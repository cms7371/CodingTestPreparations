# 2573번 빙산 https://www.acmicpc.net/problem/2573
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def count_iceberg():
    visited = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                count += 1
                visited[i][j] = True
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for o in offsets:
                        nx, ny = x + o[0], y + o[1]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 0:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return count
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            ice.append((i, j))
time = 0
result = 0
while True:
    ice_num = count_iceberg()
    if ice_num >= 2:
        result = time
        break
    elif ice_num == 0:
        break
    time += 1
    melt = []
    for x, y in ice:
        count = 0
        for o in offsets:
            nx, ny = x + o[0], y + o[1]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                count += 1
        melt.append((x, y, count))
    ice = []
    for x, y, count in melt:
        graph[x][y] = max(0, graph[x][y] - count)
        if graph[x][y] > 0:
            ice.append((x, y))
print(result)


