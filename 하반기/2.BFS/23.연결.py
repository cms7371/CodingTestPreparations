# https://www.acmicpc.net/problem/5022
from collections import deque

INF = 10 ** 9
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def explore(r, c, p1, p2, wall):
    dist = [[INF] * c for _ in range(r)]
    prev_node = [[None] * c for _ in range(r)]
    q = deque()
    q.append((*p1, 0))
    dist[p1[0]][p1[1]] = 0
    while q and dist[p2[0]][p2[1]] == INF:
        y, x, d = q.popleft()
        for dy, dx in offsets:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c and d + 1 < dist[ny][nx] and (not wall[ny][nx] or (ny == p2[0] and nx == p2[1])):
                dist[ny][nx] = d + 1
                prev_node[ny][nx] = (y, x)
                q.append((ny, nx, d + 1))
    if dist[p2[0]][p2[1]] != INF:
        wall[p2[0]][p2[1]] = True
        pn = prev_node[p2[0]][p2[1]]
        while pn:
            wall[pn[0]][pn[1]] = True
            pn = prev_node[pn[0]][pn[1]]
    return dist[p2[0]][p2[1]]


R, C = map(lambda x: int(x) + 1, input().split())
a1 = tuple(map(int, input().split()))
a2 = tuple(map(int, input().split()))
b1 = tuple(map(int, input().split()))
b2 = tuple(map(int, input().split()))
answer = INF
# a 먼저 이었을 때
c1_wall = [[False] * C for _ in range(R)]
c1_wall[b1[0]][b1[1]] = True
c1_wall[b2[0]][b2[1]] = True
c1d1 = explore(R, C, a1, a2, c1_wall)
c1d2 = explore(R, C, b1, b2, c1_wall)
answer = min(answer, c1d1 + c1d2)
# b 먼저 이었을 때
c2_wall = [[False] * C for _ in range(R)]
c2_wall[a1[0]][a1[1]] = True
c2_wall[a2[0]][a2[1]] = True
c2d1 = explore(R, C, b1, b2, c2_wall)
c2d2 = explore(R, C, a1, a2, c2_wall)
answer = min(answer, c2d1 + c2d2)
print(answer if answer < INF else "IMPOSSIBLE")
