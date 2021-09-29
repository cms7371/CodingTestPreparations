# https://www.acmicpc.net/problem/2151
from collections import deque

offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solve():
    N = int(input())
    table = [list(input()) for _ in range(N)]
    sy, sx = 0, 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == "#":
                sy, sx = i, j
    visited = [[[False] * 4 for _ in range(N)] for _ in range(N)]
    visited[sy][sx] = [True] * 4
    q = deque()
    for d in range(4):
        q.append((sy, sx, 0, d))
    while q:
        y, x, c, d = q.popleft()
        ny, nx = y + offsets[d][0], x + offsets[d][1]
        if 0 <= ny < N and 0 <= nx < N:
            if table[ny][nx] == '.' and not visited[ny][nx][d]:
                q.appendleft((ny, nx, c, d))
                visited[ny][nx][d] = True
                visited[ny][nx][(d + 2) % 4] = True
            elif table[ny][nx] == '!' and not visited[ny][nx][d]:
                q.appendleft((ny, nx, c, d))
                q.append((ny, nx, c + 1, (d + 1) % 4))
                q.append((ny, nx, c + 1, (d - 1) % 4))
                visited[ny][nx] = [True] * 4
            elif table[ny][nx] == '#':
                return c


print(solve())
