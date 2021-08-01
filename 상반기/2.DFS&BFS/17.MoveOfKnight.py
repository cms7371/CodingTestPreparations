# 7562번 나이트의 이동 https://www.acmicpc.net/problem/7562

from collections import deque
offsets = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
t = int(input())
output = []
for _ in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    visited = [[None] * n for _ in range(n)]
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 0
    while visited[end[0]][end[1]] is None:
        x, y = q.popleft()
        for o in offsets:
            nx, ny = x + o[0], y + o[1]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] is None:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    output.append(str(visited[end[0]][end[1]]))
print("\n".join(output))

