# https://www.acmicpc.net/problem/6087
from collections import deque

offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
C, R = map(int, input().split())
table = [list(input()) for _ in range(R)]
pos = []
for i in range(R):
    for j in range(C):
        if table[i][j] == 'C':
            pos.append((i, j))
dist = [[10 ** 9] * C for _ in range(R)]
q = deque()
sy, sx = pos[0]
ey, ex = pos[1]
q.append((sy, sx, -1, -1))
while q:
    y, x, d, v = q.popleft()
    if dist[y][x] > v:
        dist[y][x] = v
    for i in range(4):
        if d != -1 and i == (d + 2) % 4:
            continue
        dy, dx = offsets[i]
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and table[ny][nx] != '*':
            if i == d and dist[ny][nx] >= v:
                q.appendleft((ny, nx, i, v))
            else:
                if dist[ny][nx] >= v + 1:
                    q.append((ny, nx, i, v + 1))
for line in dist:
    for comp in line:
        print(comp if comp < 100 else 'x', end=' ')
    print("")
print(dist[ey][ex])
