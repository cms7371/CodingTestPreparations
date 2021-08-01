# 2206번 벽 부수고 이동하기 https://www.acmicpc.net/problem/2206
from collections import deque

offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(map(lambda x: -1 if x == "1" else 0, list(input()))) for _ in range(n)]
visited = [[(0, False)] * m for _ in range(n)]
q = deque()
q.append((0, 0))
visited[0][0] = (1, False)
while q and visited[-1][-1][0] == 0:
    x, y = q.popleft()
    move, passed = visited[x][y]
    for o in offsets:
        nx, ny = x + o[0], y + o[1]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                if visited[nx][ny][0] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = (move + 1, passed)
                elif visited[nx][ny][1] and not passed:
                    q.append((nx, ny))
                    visited[nx][ny] = (move + 1, passed)
            elif graph[nx][ny] == -1 and not passed:
                q.append((nx, ny))
                visited[nx][ny] = (move + 1, True)
print(visited[-1][-1][0] if visited[-1][-1][0] else -1)
