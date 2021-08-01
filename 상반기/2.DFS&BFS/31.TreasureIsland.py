# 2589번 보물섬 https://www.acmicpc.net/problem/2589
# 첫번째 시도: 꼭지점에 대해 bfs를 시도함
from collections import deque
offsets = [(1, 0, "D"), (0, 1, "R"), (-1, 0, "U"), (0, -1, "L")]
n, m = map(int, input().split())
graph = [list(map(lambda a: True if a == "L" else False, list(input()))) for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            water = []
            for dx, dy, d in offsets:
                nx, ny = i + dx, j + dy
                if not(0 <= nx < n and 0 <= ny < m and graph[nx][ny]):
                    water.append(d)
            if (len(water) == 3) or (len(water) == 2 and water not in [["D", "U"], ["R", "L"]]):
                visited = [[False] * m for _ in range(n)]
                visited[i][j] = True
                q = deque()
                q.append((i, j, 0))
                while q:
                    x, y, count = q.popleft()
                    for dx, dy, _ in offsets:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny, count + 1))
                            result = max(result, count + 1)
print(result)







