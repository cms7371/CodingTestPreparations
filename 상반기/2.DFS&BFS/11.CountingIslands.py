# 4963번 섬의 개수
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
output = []
while True:
    w, h = map(int, input().split())
    if w + h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j]:
                q = deque()
                q.append((i, j))
                graph[i][j] = 0
                result += 1
                while q:
                    x, y = q.popleft()
                    for o in offsets:
                        nx, ny = x + o[0], y + o[1]
                        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny]:
                            graph[nx][ny] = 0
                            q.append((nx, ny))
    output.append(str(result))

print("\n".join(output))


