# https://www.acmicpc.net/problem/2178
from collections import deque
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
graph[0][0] = 0
q = deque()
q.append((0, 0, 1))
while q:
    y, x, moves = q.popleft()
    for dy, dx in offsets:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
            if ny == n - 1 and nx == m - 1:
                print(moves + 1)
                q = False
                break
            else:
                graph[ny][nx] = 0
                q.append((ny, nx, moves + 1))
